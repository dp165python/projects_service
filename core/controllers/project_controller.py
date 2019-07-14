import uuid

from flask_restful import abort

from core.controllers.error_handlers import handle_schema_error
from core.models import Projects, Data
from core.controllers.session_handler import dbconnect, Session


class ProjectController:

    def __init__(self, data, errors):
        self._data = data
        self._errors = errors

    @handle_schema_error
    @dbconnect
    def create_project(self):

        session = Session()
        project_name = self._data['name']
        contract_id = self._data['contract_id']
        project = Projects(name=project_name, contract_id=contract_id, status='default')
        session.add(project)

        return contract_id

    @handle_schema_error
    @dbconnect
    def update_project_status(self, id):
        session = Session()
        status = self._data['status']
        project = Projects.query.filter(Projects.id == id).first()

        if not project:
            abort(404, error='Project doesn\'t exist')

        session.query(Projects).filter(Projects.id == id). \
            update({'status': status})

        return 'updated'

    @handle_schema_error
    @dbconnect
    def update_contract_id(self, id):
        session = Session()
        contract_id = self._data['contract_id']
        project = Projects.query.filter(Projects.id == id).first()

        if not project:
            abort(404, error='Project doesn\'t exist')

        session.query(Projects).filter(Projects.id == id). \
            update({'contract_id': contract_id})

        return 'updated'

    @handle_schema_error
    def post_data(self, id):
        session = Session()
        if not Projects.query.filter(Projects.id == id).first():
            abort(404, error='Project doesn\'t exist')

        for data in self._data['data']:
            project_data = Data(
                project_id=uuid.UUID(id),
                field_1=data['field_1'],
                field_2=data['field_2'],
                field_3=data['field_3'],
                field_4=data['field_4'],
                field_5=data['field_5']
            )
            session.add(project_data)
        return 'added'

    @staticmethod
    @dbconnect
    def delete_project(id):
        session = Session()
        deleted_project = Projects.query.filter(Projects.id == id).first()

        if not deleted_project:
            abort(404, error='Project doesn\'t exist')

        session.query(Projects).filter(Projects.id == id). \
            delete()

        return deleted_project




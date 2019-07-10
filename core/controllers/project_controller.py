import uuid

from flask_restful import abort

from core.controllers.error_handlers import handle_schema_error
from core.models import Projects, Data
from core.utils.session import session


class ProjectController:

    def __init__(self, data, errors):
        self._data = data
        self._errors = errors

    @handle_schema_error
    def create_project(self):
        project_name = self._data['name']
        contract_id = self._data['contract_id']
        project = Projects(name=project_name, contract_id=contract_id, status='default')

        with session() as db:
            db.add(project)

        return Projects.query.filter(Projects.contract_id == contract_id).first()

    @handle_schema_error
    def update_project_status(self, id):
        status = self._data['status']
        project = Projects.query.filter(Projects.id == id).first()

        if not project:
            abort(404, error='Project doesn\'t exist')

        with session():
            project.status = status

        return 'updated'

    @handle_schema_error
    def update_contract_id(self, id):
        contract_id = self._data['contract_id']
        project = Projects.query.filter(Projects.id == id).first()

        if not project:
            abort(404, error='Project doesn\'t exist')

        with session():
            project.contract_id = contract_id

        return 'updated'

    @handle_schema_error
    def post_data(self, id):
        if not Projects.query.filter(Projects.id == id).first():
            abort(404, error='Project doesn\'t exist')

        with session() as db:
            for data in self._data['data']:
                project_data = Data(
                    project_id=uuid.UUID(id),
                    field_1=data['field_1'],
                    field_2=data['field_2'],
                    field_3=data['field_3'],
                    field_4=data['field_4'],
                    field_5=data['field_5'],
                    field_6=data['field_6'],
                    field_7=data['field_7'],
                    field_8=data['field_8'],
                    field_9=data['field_9'],
                    field_10=data['field_10']
                )
                db.add(project_data)
        return 'added'

    @staticmethod
    def delete_project(id):
        deleted_project = Projects.query.filter(Projects.id == id).first()

        if not deleted_project:
            abort(404, error='Project doesn\'t exist')

        with session() as db:
            db.query(Projects).filter(Projects.id == id). \
                delete()

        return deleted_project




from flask_restful import abort

from core.models import Projects
from core.utils.session import session


class ProjectController:
    def __init__(self, data):
        self._data, self._errors = data
        print(data)

    def create_project(self,):
        self._schema_error_handler()

        try:
            project_name = self._data['name']
            contract_id = self._data['contract_id']
        except KeyError:
            abort(404, error='not enough data')

        project = Projects(name=project_name, contract_id=contract_id, status='default')

        with session() as db:
            db.add(project)

        return Projects.query.filter(Projects.contract_id == contract_id).first()

    def _schema_error_handler(self):
        if self._errors:
            print(self._errors)
            abort(404, error=self._errors)

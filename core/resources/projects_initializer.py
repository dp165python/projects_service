from flask import request
from flask_restful import Resource, abort

from core.models import Projects
from core.utils.schemas import ProjectSchema
from core.utils.session import session


# /projects
class ProjectsInitializer(Resource):
    project_schema = ProjectSchema()

    def get(self):
        projects = Projects.query.all()
        return {'data': ProjectsInitializer.project_schema.dump(projects, many=True).data}, 200

    def post(self):
        data, errors = ProjectsInitializer.project_schema.load(request.json)

        if errors:
            abort(404)

        project_name = data['name']
        contract_id = data['contract_id']
        project = Projects(name=project_name, contract_id=contract_id, status='default')

        with session() as db:
            db.add(project)

        added_project = Projects.query.filter(Projects.contract_id == contract_id).first()

        return {'status': 'create_successfully', 'id': str(added_project.id)}, 201

from flask import request
from flask_restful import Resource

from core.controllers.project_controller_ import ProjectController
from core.models import Projects
from core.utils.schemas import ProjectSchema


# /projects
class ProjectsInitializer(Resource):
    project_schema = ProjectSchema()

    def get(self):
        projects = Projects.query.all()
        return {'data': ProjectsInitializer.project_schema.dump(projects, many=True).data}, 200

    def post(self):
        data, errors = ProjectsInitializer.project_schema.load(request.json)

        contract_id_of_added_project = ProjectController(data, errors).create_project()
        added_project = Projects.query.filter(Projects.contract_id == contract_id_of_added_project).first()

        return {'status': 'create', 'project': ProjectsInitializer.project_schema.dump(added_project).data}, 201

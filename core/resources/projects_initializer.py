from flask import request
from flask_restful import Resource, abort

from core.controllers.project_controller import ProjectController
from core.controllers.values_to_return import ProjectData
from core.models import Projects
from core.utils.schemas import ProjectSchema


# /projects
class ProjectsInitializer(Resource):
    project_schema = ProjectSchema()

    def get(self):
        projects = Projects.query.all()
        return {
            'projects': [ProjectData(project_data).transform_project_data_into_dict() for project_data in projects]
        }, 200

    def post(self):
        data, errors = ProjectsInitializer.project_schema.load(request.json)
        contract_id = ProjectController(data, errors).create_project()

        added_project = Projects.query.filter(Projects.contract_id == contract_id).first()
        return ProjectData(added_project).transform_project_data_into_dict(), 201

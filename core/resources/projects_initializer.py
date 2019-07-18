from flask import request
from flask_restful import Resource

from core.controllers.project_controller import ProjectsController
from core.controllers.values_to_return import ProjectData
from core.models.schemas import ProjectSchema


class ProjectsInitializer(Resource):
    project_schema = ProjectSchema()

    def get(self):
        controller = ProjectsController()
        projects = controller.get_projects()
        return {
               'projects': [ProjectData(project_data).transform_project_data_into_dict() for project_data in projects]
        }, 200

    def post(self):
        data, errors = ProjectsInitializer.project_schema.load(request.json)
        controller = ProjectsController()

        project = controller.create_project(data, errors)
        return ProjectData(project).transform_project_data_into_dict(), 201


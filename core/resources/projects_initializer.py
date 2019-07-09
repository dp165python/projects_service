from flask import request
from flask_restful import Resource, abort

from core.controllers.project_controller import ProjectController
from core.models import Projects
from core.utils.schemas import ProjectSchema


# /projects
class ProjectsInitializer(Resource):
    project_schema = ProjectSchema()

    def get(self):
        projects = Projects.query.all()
        return {'data': ProjectsInitializer.project_schema.dump(projects, many=True).data}, 200

    def post(self):
        data = ProjectsInitializer.project_schema.load(request.json)

        added_project = ProjectController(data).create_project()

        return {'status': 'create', 'project': ProjectsInitializer.project_schema.dump(added_project).data}, 201

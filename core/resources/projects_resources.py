from flask import request
from flask_restful import Resource

from core.controllers.projects_controller import ProjectsController
from core.controllers.values_controller import ProjectData
from core.models.schemes import ProjectSchema, ContractIdSchema, StatusSchema, DataSchema


class BaseProjectsController(Resource):
    controller = ProjectsController()


class ProjectsInitializer(BaseProjectsController):

    def get(self):
        projects = self.controller.get_projects()
        return {
                'projects': [ProjectData(project_data).transform_project_data_into_dict() for project_data in projects]
        }, 200

    def post(self):
        data, errors = ProjectSchema().load(request.json)
        project = self.controller.create_project(data, errors)
        return ProjectData(project).transform_project_data_into_dict(), 201


class ProjectsResources(BaseProjectsController):

    def get(self, id):
        project = self.controller.get_project_by_id(id)
        return ProjectData(project).transform_project_data_into_dict(), 200

    def patch(self, id):
        data, errors = ContractIdSchema().load(request.json)
        project = self.controller.update_contract_id(id, data, errors)
        return ProjectData(project).transform_project_data_into_dict(), 200

    def delete(self, id):
        project = self.controller.delete_project(id)
        return ProjectData(project).transform_project_data_into_dict(), 200


class ProjectsStatusUpdater(BaseProjectsController):

    def patch(self, id):
        data, errors = StatusSchema().load(request.json)
        project = self.controller.update_project_status(id, data, errors)
        return ProjectData(project).transform_project_data_into_dict(), 200


class ProjectsDataResources(BaseProjectsController):

    def post(self, id):
        data, errors = DataSchema().load(request.json)
        data_len = self.controller.save_projects_data(id, data, errors)
        return {'project_id': id, 'objects_wrote': data_len}, 201

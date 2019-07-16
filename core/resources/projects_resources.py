from flask import request
from flask_restful import Resource, abort

from core.controllers.project_controller import ProjectController
from core.controllers.values_to_return import ProjectData
from core.models import Projects
from core.utils.schemas import ContractIdSchema


# /projects/<id>
class ProjectsResources(Resource):
    def get(self, id):
        project = Projects.query.filter_by(id=id).first()
        if not project:
            abort(404, error="No such project")

        return ProjectData(project).transform_project_data_into_dict(), 200

    # update contract_id
    def patch(self, id):
        data, errors = ContractIdSchema().load(request.json)
        contract_id = ProjectController(data, errors).update_contract_id(id)
        updated_project = Projects.query.filter(Projects.contract_id == contract_id).first()
        return ProjectData(updated_project).transform_project_data_into_dict(), 200

    def delete(self, id):
        deleted_project = ProjectController.delete_project(id)
        return ProjectData(deleted_project).transform_project_data_into_dict(), 200


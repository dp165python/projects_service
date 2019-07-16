from flask import request
from flask_restful import Resource

from core.controllers.values_to_return import ProjectData
from core.models import Projects
from core.utils.schemas import StatusSchema, ProjectSchema
from core.controllers.project_controller import ProjectController


# /projects/<id>/status
class StatusUpdater(Resource):

    def patch(self, id):
        data, errors = StatusSchema().load(request.json)
        ProjectController(data, errors).update_project_status(id)
        updated_project = Projects.query.filter(Projects.id == id).first()

        return ProjectData(updated_project).transform_project_data_into_dict(), 200

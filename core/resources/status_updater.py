from flask import request
from flask_restful import Resource, abort

from core.models import Projects
from core.utils.schemas import StatusSchema, ProjectSchema
from core.controllers.project_controller import ProjectController


# /projects/<id>/status
class StatusUpdater(Resource):

    def patch(self, id):
        data, errors = StatusSchema().load(request.json)

        status = ProjectController(data, errors).update_project_status(id)

        updated_project = Projects.query.filter(Projects.id == id).first()

        if not updated_project:
            abort(404, error='Project doesn\'t exist')

        return {'status': status, 'project': ProjectSchema().dump(updated_project).data}, 200

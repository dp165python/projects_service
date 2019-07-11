from flask import request
from flask_restful import Resource, abort

from core.controllers.project_controller import ProjectController
from core.models import Projects
from core.utils.schemas import ProjectSchema


# /projects/<id>
class ProjectsResources(Resource):
    project_schema = ProjectSchema()

    def get(self, id):
        project = Projects.query.filter_by(id=id).first()

        if not project:
            abort(404, error="No such project")
        return ProjectsResources.project_schema.dump(project).data, 200

    # update contract_id
    def patch(self, id):
        data, errors = ProjectsResources.project_schema.load(request.json)

        status = ProjectController(data, errors).update_contract_id(id)
        updated_project = Projects.query.filter(Projects.id == id).first()

        if not updated_project:
            abort(404, error="No such project")

        return {'status': status, 'project': ProjectsResources.project_schema.dump(updated_project).data}, 200

    def delete(self, id):
        deleted_project = Projects.query.filter_by(id=id).delete()
        # deleted_project = ProjectController.delete_project(id)

        if not deleted_project:
            abort(404, error="No such project")

        return {'status': 'deleted', 'project': ProjectsResources.project_schema.dump(deleted_project).data}, 200

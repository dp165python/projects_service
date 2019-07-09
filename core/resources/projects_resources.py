from flask import request
from flask_restful import Resource, abort

from core.models import Projects
from core.utils.schemas import ProjectSchema
from core.utils.session import session


# /projects/<id>
class ProjectsResources(Resource):
    project_schema = ProjectSchema()

    def get(self, id):
        project = Projects.query.filter_by(id=id).first()

        if not project:
            abort(404, "No such project")

        return {
                   'name': project.name,
                   'contract_id': str(project.contract_id),
                   'status': project.name
               }, 200

    # update contract_id
    def put(self, id):
        data, errors = ProjectsResources.project_schema.load(request.json)

        if errors:
            abort(404, 'error')

        contract_id = data['contract_id']
        with session() as db:
            db.query(Projects).filter(Projects.id == id). \
                update({'contract_id': contract_id})

        return {'status': 'updated'}, 200

    def delete(self, id):
        with session() as db:
            db.query(Projects).filter(Projects.id == id). \
                delete()

        return {'status': 'deleted successfully'}, 200

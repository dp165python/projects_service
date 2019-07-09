from flask import request
from flask_restful import Resource, abort

from core.models import Projects
from core.utils.schemas import StatusSchema
from core.utils.session import session


# /projects/<id>/status
class StatusUpdater(Resource):
    status_schema = StatusSchema()

    def put(self, id):
        data, errors = StatusSchema.status_schema.load(request.json)

        if errors:
            abort(404, 'invalid status')

        status = data['status']
        with session() as db:
            db.query(Projects).filter(Projects.id == id). \
                update({'status': status})

        return {'status': 'status_updated_successfully'}, 200

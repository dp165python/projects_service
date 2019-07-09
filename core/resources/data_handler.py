import uuid

from flask import request
from flask_restful import Resource, abort

from core.models import Data
from core.utils.schemas import DataSchema
from core.utils.session import session


# /projects/<id>/data/
class DataHandler(Resource):
    data_schema = DataSchema()

    def post(self, id):
        data, errors = DataHandler.data_schema.load(request.json)

        if errors:
            abort(404, 'Invalid data')

        with session() as db:
            for data in data['data']:
                project_data = Data(
                    project_id=uuid.UUID(id),
                    field_1=data['field_1'],
                    field_2=data['field_2'],
                    field_3=data['field_3'],
                    field_4=data['field_4'],
                    field_5=data['field_5']
                )
                db.add(project_data)

        return {'status': 'write_all_data'}, 201

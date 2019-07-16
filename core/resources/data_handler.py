import uuid

from core.controllers.project_controller import ProjectController
from core.utils.schemas import DataSchema

from flask import request
from flask_restful import Resource


# /projects/<id>/data/
class DataHandler(Resource):

    def post(self, id):
        data, errors = DataSchema().load(request.json)

        status = ProjectController(data, errors).post_data(id)

        return {'status': status}, 201

# from uuid import UUID
import uuid
from flask import request
from flask_restful import Resource

from core.models import Projects, Data
from core.controllers.data_controller import CalculationDataController


# /projects/<id>/calculations
class ProjectsCalculation(Resource):

    def get(self, project_id):
        pass

        """
        Method to fetch data of the particular project for calculation
        :param project_id: an id of the project
        """
        # controller = CalculationDataController()
        # print(';lkjasd')
        # return controller.get_data_by_id(project_id)

    # def post(self, id):
    #     """
    #     Method to retrieve  calculated data of the particular project
    #     :param id: an id of the project
    #     """
    #
    #     # obtain certain project
    #     project = Projects.query.filter_by(id=uuid.UUID(id)).first()
    #     if not project:
    #         abort(404, "Project doesn\'t exist")
    #
    #     # deserialize input json
    #     entry_data = request.get_json()
    #     if not entry_data:
    #         return {"error": "No input data provided"}, 400
    #     result = entry_data["result"]
    #     return {"result": result}, 200

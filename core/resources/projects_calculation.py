from core.models.models import Data
from flask import request
from flask_restful import Resource

from core.controllers.data_to_calculation_controller import DataToCalculationController
from core.controllers.values_controller import ProjectData
from core.controllers.data_controller import Data
from core.models.schemas import ProjectSchema


class BaseDataController(Resource):
    controller = DataToCalculationController()


class ProjectsDataToCalculation(BaseDataController):
    """
    Method to fetch data of the particular project for calculation
    :param id: an id of the project
    """
    def get(self, id):
        data = self.controller.get_project_data_by_id(id)
        return Data(data).transform_data_into_dict(), 200

        # return {
        #            'project': ProjectsCalculation.project_schema.dump(project).data,
        #            'data': ProjectsCalculation.nested_schema.dump(data, many=True).data
        #        }, 200

    # def post(self, id):

    def post(self, id):
        """
        Method to retrieve  calculated data of the particular project
        :param id: an id of the project
        """
        data, errors = ProjectSchema().load(request.json)
        project = self.controller.receive_calculation_result(id, data, errors)
        return ProjectData(project).transform_project_data_into_dict(), 201

from flask import request
from flask_restful import Resource

from core.controllers.data_to_calculation_controller import DataToCalculationController
from core.controllers.values_controller import ProjectData
from core.models.schemas import ProjectSchema, DataNestedSchema


nested_schema = DataNestedSchema()
project_schema = ProjectSchema(exclude=["status", "name"])


class BaseDataController(Resource):
    controller = DataToCalculationController()


class ProjectsDataToCalculation(BaseDataController):

    def get(self, id):
        """
        Method to fetch data of the particular project for calculation
        :param id: an id of the project
        """
        project = self.controller.get_project_by_id(id=id)
        data = self.controller.get_project_data_by_id(id)

        return {'project': project_schema.dump(project).data,
                'data': nested_schema.dump(data, many=True).data}, 200

    def post(self, id):
        """
        Method to retrieve  calculated data of the particular project
        :param id: an id of the project
        """
        data, errors = ProjectSchema().load(request.json)
        project = self.controller.receive_calculation_result(id, data, errors)

        return ProjectData(project).transform_project_data_into_dict(), 201


class ProjectsDataToCalculationPage(BaseDataController):

    def get(self, id, page_num):
        """
        Method to fetch paginated data of the particular project for calculation
        :param id: an id of the project
        :param page_num: a page number of the paginated data
        """
        project = self.controller.get_project_by_id(id=id)
        data = self.controller.get_project_data_by_id_page(id, page_num)

        return {'project': project_schema.dump(project).data,
                'data': nested_schema.dump(data, many=True).data}, 200

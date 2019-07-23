from flask import g, abort
from core.models.models import Projects, Data
from paginator import Paginator


class DataToCalculationController:
    @staticmethod
    def get_project_by_id(id):
        project = g.session.query(Projects).filter(Projects.id == id).first()
        if not project:
            abort(404, 'Project with this id does not exist')
        return project

    def get_project_data_by_id(self, id):
        project = self.get_project_by_id(id=id)

        new_status = "calculation"
        project.status = new_status

        data = g.session.query(Data).filter(Data.project_id == id).all()
        if not data:
            abort(404, 'This project_id data is empty')
        return data

    def get_project_data_by_id_page(self, id, page_num):
        project = self.get_project_by_id(id=id)

        new_status = "calculation"
        project.status = new_status

        if not page_num:
            abort(404, 'Incorrect page info')

        data = g.session.query(Data).filter(Data.project_id == id).all()
        if not data:
            abort(404, 'This project_id data is empty')
        data_paginated = Paginator(data, page=page_num, per_page=2)

        return data_paginated.items

    def receive_calculation_result(self, id, data, errors):
        if errors:
            abort(404, errors)

        result = data['result']
        if not result:
            return {"warning": "No calculation result provided"}, 400

        project = self.get_project_by_id(id=id)
        if not project:
            abort(404, 'Project with this id does not exist')

        return project

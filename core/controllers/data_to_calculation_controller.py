from flask import g, abort
from core.models.models import Projects, Data


class DataToCalculationController:

    @staticmethod
    def get_project_data_by_id(id):

        project = g.session.query(Projects).filter(Projects.id == id).first()
        if not project:
            abort(404, 'Project with this id does not exist')

        new_status = "calculation"
        project.status = new_status

        data = g.session.query(Data).filter(Data.project_id == id).all()
        if not data:
            abort(404, 'Data with this project_id does not exist')
            # return {"error": "Project doesn\'t exist"}, 404
        return data

    @staticmethod
    def receive_calculation_result(id, data, errors):
        if errors:
            abort(404, errors)

        result = data['result']
        if not result:
            return {"warning": "No calculation result provided"}, 400

        project = g.sesison.query(Projects).filter(Projects.id == id).first()
        if not project:
            abort(404, 'Project with this id does not exist')

        return project

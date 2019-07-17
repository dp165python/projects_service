from uuid import UUID

from flask import g
from flask_restful import abort
from core.models import Projects, Data
from core.utils.schemas import ProjectSchema, DataNestedSchema
from core.utils.session import session


class CalculationDataController:
    # project_schema = ProjectSchema()
    # nested_schema = DataNestedSchema()

    def get_data_by_id(self, project_id) -> dict:
        project = Projects.query.filter_by(id=project_id).first()
        print(project)
        if not project:
            # abort(404, "No such project")
            return {"error": "Project doesn\'t exist"}, 404

        new_status = "calculation"
        # with session() as db:
        #     db.query(Projects).filter(Projects.id == project_id). \
        #         update({'status': new_status})

        data = Data.query.filter_by(project_id=project_id).all()
        if not data:
            abort(400, "No input data provided")
        print('jdf')
        # return {
        #            'project': dict(project),
        #            'data': dict(data)
        #        }, 200

        # user = self.get_user(user_id)
        # data = dict(user)
        # del data['token']
        # return data

    # def get_users(self):
    #     return g.session.query(Users).all()
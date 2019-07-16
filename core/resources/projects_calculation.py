import uuid

from flask import request
from flask_restful import Resource, abort

from core.models import Projects, Data
from core.utils.schemas import ProjectSchema, DataNestedSchema
from core.utils.session import session


# /projects/<id>/calculations
class ProjectsCalculation(Resource):
    project_schema = ProjectSchema()
    nested_schema = DataNestedSchema()

    def get(self, id):

        """
        Method to fetch data of the particular project for calculation
        :param id: an id of the project
        """
        project = Projects.query.filter_by(id=id).first()
        if not project:
            # abort(404, "No such project")
            return {"error": "Project doesn\'t exist"}, 404

        new_status = "calculation"
        with session() as db:
            db.query(Projects).filter(Projects.id == id). \
                update({'status': new_status})

        data = Data.query.filter_by(project_id=id).all()
        if not data:
            abort(400, "No input data provided")

        return {
                   'project': ProjectsCalculation.project_schema.dump(project).data,
                   'data': ProjectsCalculation.nested_schema.dump(data, many=True).data
               }, 200

    def post(self, id):
        """
        Method to retrieve  calculated data of the particular project
        :param id: an id of the project
        """

        # obtain certain project
        project = Projects.query.filter_by(id=uuid.UUID(id)).first()
        if not project:
            abort(404, "Project doesn\'t exist")

        # deserialize input json
        entry_data = request.get_json()
        if not entry_data:
            return {"error": "No input data provided"}, 400
        result = entry_data["result"]
        return {"result": result}, 200

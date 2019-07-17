from flask_restful import Resource, abort

from core.models import Data, Projects
from core.utils.schemas import DataNestedSchema
from core.utils.session import session


# /projects/<id>/calculations/<int:page_num>
class ProjectsCalculationPage(Resource):
    nested_schema = DataNestedSchema()

    def get(self, id, page_num):
        project = Projects.query.filter_by(id=id).first()
        if not project:
            abort(404, error='Project doesn\'t exist')
            # return {"error": "Project doesn\'t exist"}, 404

        new_status = 'calculation'
        with session() as db:
            db.query(Projects).filter(Projects.id == id). \
                update({'status': new_status})

        data_query = Data.query.filter_by(project_id=id).paginate(page=page_num, error_out=False, max_per_page=2)
        if not data_query:
            abort(400, "No input data provided")

        data = data_query.items

        return {
                'data': ProjectsCalculationPage.nested_schema.dump(data, many=True).data,
                'total_data_items': data_query.total,
                'current_page': data_query.page,
                'per_page': data_query.per_page
               }, 200

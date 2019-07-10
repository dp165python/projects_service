import uuid

from flask import request, abort, jsonify
from flask_restful import Resource

from .models import Projects, Data
from .utils.schemas import ProjectSchema, DataSchema, StatusSchema, DataNestedSchema
from .utils.session import session

project_schema = ProjectSchema()
status_schema = StatusSchema()
data_schema = DataSchema()
nested_schema = DataNestedSchema()


# /projects
class ProjectsInitializer(Resource):
    def get(self):
        projects = Projects.query.all()
        return {'data': project_schema.dump(projects, many=True).data}, 200

    def post(self):
        data, errors = project_schema.load(request.json)

        if errors:
            abort(404, 'not enough data')

        project_name = data['name']
        contract_id = data['contract_id']
        project = Projects(name=project_name, contract_id=contract_id, status='default')

        with session() as db:
            db.add(project)
            project_id = db.query(Projects).filter(Projects.contract_id == contract_id).first()

        return {'status': 'create_successfully', 'id': str(project_id)}, 201


# /projects/<id>
class ProjectsResources(Resource):
    def get(self, id):
        project = Projects.query.filter_by(id=id).first()

        if not project:
            abort(404, "No such project")

        return {
            'name': project.name,
            'contract_id': str(project.contract_id),
            'status': project.name
        }, 200

    # update contract_id
    def put(self, id):
        data, errors = project_schema.load(request.json)

        if errors:
            abort(404, 'error')

        contract_id = data['contract_id']
        with session() as db:
            db.query(Projects).filter(Projects.id == id). \
                update({'contract_id': contract_id})

        return {'status': 'updated'}, 200

    def delete(self, id):
        with session() as db:
            db.query(Projects).filter(Projects.id == id). \
                delete()

        return {'status': 'deleted successfully'}, 200


# /projects/<id>/status
class StatusUpdater(Resource):
    def put(self, id):
        data, errors = status_schema.load(request.json)

        if errors:
            abort(404, 'invalid status')

        status = data['status']
        with session() as db:
            db.query(Projects).filter(Projects.id == id). \
                update({'status': status})

        return {'status': 'status_updated_successfully'}, 200


# /projects/<id>/data/
class DataHandler(Resource):
    def post(self, id):
        data, errors = data_schema.load(request.json)

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



# TODO
# /projects/<id>/calculations
class ProjectsCalculation(Resource):
    def get(self, id):

        """
        Method to fetch data of the particular project for calculation
        :param id: an id of the project
        """
        project = Projects.query.filter_by(id=id).first()
        if not project:
            abort(404, "No such project")

        new_status = "calculation"
        with session() as db:
            db.query(Projects).filter(Projects.id == id). \
                update({'status': new_status})

        data = Data.query.filter_by(project_id=id).all()
        if not data:
            abort(400, "No input data provided")

        return {'project': project_schema.dump(project).data, 'data': nested_schema.dump(data, many=True).data}, 200

    def post(self, id):
        """
        Method to retrieve  calculated data of the particular project
        :param id: an id of the project
        """

        # obtain certain project
        project = Projects.query.filter_by(id=uuid.UUID(id)).first()
        if not project:
            abort(404, "No such project")

        # deserialize input json
        entry_data = request.get_json()
        if not entry_data:
            return {"message": "No input data provided"}, 400
        result = entry_data["result"]
        return {"result": result}, 200


# class ProjectsCalculationPage(Resource):
#     def get(self, id, page_num):
#
#         """
#         Method to fetch data of the particular project for calculation
#         :param id: an id of the project
#         """
#         project = Projects.query.filter_by(id=id).first()
#         if not project:
#             abort(404, "No such project")
#
#         new_status = "calculation"
#         with session() as db:
#             db.query(Projects).filter(Projects.id == id). \
#                 update({'status': new_status})
#
#         data = Data.query.filter_by(project_id=id).paginate(per_page=5, page=page_num, error_out=True)
#         if not data:
#             abort(400, "No input data provided")
#
#         return {'project': project_schema.dump(project).data, 'data': nested_schema.dump(data, many=True).data}, 200

# TODO
class ProjectsCalculationPage(Resource):
    def get(self, id, page_num):
        paginated = self.get_paginated_list(Data, '/projects/<id>/calculations/page',
                                          start=request.args.get('start', 1),
                                          limit=request.args.get('limit', 3))
        return {'data': nested_schema.dump(paginated, many=True).data}, 200

    def get_paginated_list(self, klass, url, start, limit):
        # check if page exists
        results = klass.query.all()
        count = len(results)
        if (count < start):
            abort(404)
        # make response
        obj = {}
        obj['start'] = start
        obj['limit'] = limit
        obj['count'] = count
        # make URLs
        # make previous url
        if start == 1:
            obj['previous'] = ''
        else:
            start_copy = max(1, start - limit)
            limit_copy = start - 1
            obj['previous'] = url + '?start=%d&limit=%d' % (start_copy, limit_copy)
        # make next url
        if start + limit > count:
            obj['next'] = ''
        else:
            start_copy = start + limit
            obj['next'] = url + '?start=%d&limit=%d' % (start_copy, limit)
        # finally extract result according to bounds
        obj['results'] = results[(start - 1):(start - 1 + limit)]
        return obj
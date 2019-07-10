import uuid

from flask import request
from flask_restful import Resource, abort

from core.models import Data
from core.utils.schemas import DataNestedSchema


nested_schema = DataNestedSchema()


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
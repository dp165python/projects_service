# python -m unittest test_api to run tests

import unittest
from flask import json
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from core.app import app


class TestMyAppCRUD(unittest.TestCase):
    # executed prior to each test
    def setUp(self):
        self.app = app.test_client()

    app.config['TESTING'] = True
    # app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://eugene:1401@localhost/test_api'
    # test-db settings
    engine = create_engine('postgresql://eugene:1401@localhost/test_api')
    base = declarative_base()

    # run to create tables on server
    base.metadata.create_all(engine)

    # executed after each test
    def tearDown(self):
        # run to drop all tables
        # base = declarative_base()
        # base.metadata.drop_all(db)

        # db.drop_all()
        pass

    def test_getting_all_projects(self):
        # HTTP GET request to the application on certain path
        prj = self.app.get('/projects')

        # assert the status code and type of response
        self.assertEqual(prj.status_code, 200)
        self.assertEqual(prj.content_type, 'application/json')

    # def test_initialize_projects_post(self):
    #     # Test data:
    #     mock_data = {
    #         'status': 'create_schema',
    #         'name': 'eugene',
    #         'contract_id': '28f441a0-d0b1-4b22-b16b-c1e718dab64d'
    #     }
    #
    #     # HTTP POST request
    #     prj = self.app.post('/projects', data=json.dumps(mock_data), content_type='application/json')
    #     self.assertEqual(prj.content_type, 'application/json')
    #     self.assertEqual(prj.status_code, 201)

    # def test_getting_certain_project(self, _id='a71b7ff7-120d-487a-ba4e-df5fc49fbe39'):
    #     # HTTP GET request to the application on certain path
    #     prj = self.app.get('/projects/{}'.format(_id))
    #     self.assertEqual(prj.status_code, 200)

    def test_getting_certain_project_denial(self, _id='00000000-0000-0000-0000-000000000000'):
        # HTTP GET request with incorrect id
        prj = self.app.get('/projects/{}'.format(_id))
        self.assertEqual(prj.data, b'{"error": "Project doesn\'t exist"}\n')
        self.assertEqual(prj.status_code, 404)

    # def test_patching_certain_project(self, _id='a71b7ff7-120d-487a-ba4e-df5fc49fbe39'):
    #     # HTTP PATCH request to the application on certain path
    #     prj = self.app.patch('/projects/{}'.format(_id))
    #     self.assertEqual(prj.status_code, 200)

    def test_patching_certain_project_denial(self, _id='00000000-0000-0000-0000-000000000000'):
        # Test data:
        mock_data = {
                'contract_id': '28f441a0-d0b1-4b22-b16b-c1e718dab64d'
            }
        # HTTP PATCH request with incorrect id
        prj = self.app.patch('/projects/{}'.format(_id), data=json.dumps(mock_data), content_type='application/json')
        self.assertEqual(prj.data, b'{"error": "Project doesn\'t exist"}\n')
        self.assertEqual(prj.status_code, 404)

    # def test_delete_certain_project(self, _id='e3cb6cec-2945-4490-828d-f8267d925ca3'):
    #     # HTTP DELETE request to the application on certain path
    #     prj = self.app.delete('/projects/{}'.format(_id))
    #     self.assertEqual(prj.status_code, 200)

    def test_deleting_certain_project_denial(self, _id='00000000-0000-0000-0000-000000000000'):
        # HTTP DELETE request with incorrect id
        prj = self.app.delete('/projects/{}'.format(_id))
        self.assertEqual(prj.data, b'{"error": "Project doesn\'t exist"}\n')
        self.assertEqual(prj.status_code, 404)

    def test_posting_certain_project_data_denial(self, _id='00000000-0000-0000-0000-000000000000'):
        # HTTP POST request with incorrect id
        prj = self.app.post('/projects/{}/data'.format(_id))
        self.assertEqual(prj.data, b'{"error": "Project doesn\'t exist"}\n')
        self.assertEqual(prj.status_code, 404)

    # def test_posting_certain_project_data_success(self, _id='a71b7ff7-120d-487a-ba4e-df5fc49fbe39'):
    #     # Test data:
    #     mock_data = {
    #             'field_1': '777',
    #             'field_2': '333',
    #             'field_3': '3.1415',
    #             'field_4': '0',
    #             'field_5': 'Give us a decent job'
    #     }
    #
    #     # HTTP POST request with incorrect id
    #     prj = self.app.post('/projects/{}/data'.format(_id), data=json.dumps(mock_data), content_type='application/json')
    #     self.assertEqual(prj.status_code, 201)

    def test_updating_certain_project_denial(self, _id='00000000-0000-0000-0000-000000000000'):
        # Test data:
        mock_data = {
                'status': 'updated'
            }
        # HTTP PATCH request with incorrect id
        prj = self.app.patch('/projects/{}/status'.format(_id), data=json.dumps(mock_data), content_type='application/json')
        self.assertEqual(prj.data, b'{"error": "Project doesn\'t exist"}\n')
        self.assertEqual(prj.status_code, 404)

    def test_getting_all_calculations_denial(self):
        # HTTP GET request to the application on certain path
        prj = self.app.get('/projects/00000000-0000-0000-0000-000000000000/calculations')

        # assert the status code and type of response
        self.assertEqual(prj.status_code, 404)
        self.assertEqual(prj.content_type, 'application/json')

    def test_getting_calculations_page_denial(self):
        # HTTP GET request to the application on certain path
        prj = self.app.get('/projects/00000000-0000-0000-0000-000000000000/calculations/1')

        # assert the status code and type of response
        self.assertEqual(prj.status_code, 404)
        self.assertEqual(prj.content_type, 'application/json')

    # def test_add(self):
    #     rv = self.app.get('/add/2/3')
    #     self.assertEqual(rv.status, '200 OK')
    #     self.assertEqual(rv.data, '5')
    #
    # def test_404(self):
    #     rv = self.app.get('/other')
    #     self.assertEqual(rv.status, '404 NOT FOUND')

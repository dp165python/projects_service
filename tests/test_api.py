# python -m unittest test_api to run tests

import unittest
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from core.app import app
from core.config import db



# TEST_DB = 'test_api.db'
# BASE = declarative_base()


class TestMyAppCRUD(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()

    app.config['TESTING'] = True
    # app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://eugene:1401@localhost/test_api'
    engine = create_engine('postgresql://eugene:1401@localhost/test_api')

    # db = sqlalchemy.create_engine(postgres_uri())
    base = declarative_base()

    # run to create tables on server
    base.metadata.create_all(engine)

    # app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'db.sqlite')
    # self.app = app.test_client()
    # db.drop_all()
    # db.create_all()

    # executed prior to each test
    # def setUp(self):
    #     app.config['TESTING'] = True
    #     app.config['WTF_CSRF_ENABLED'] = False
    #     app.config['DEBUG'] = False
    #     app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://eugene:1401@localhost/test_api'
    #
    #     # db.create_all()
    #     with app.app_context():
    #         db.init_app(app)
    #         migrate.init_app(app, db)
    #     self.app = app.test_client()


    # executed after each test
    def tearDown(self):
        # run to drop all tables
        # base = declarative_base()
        # base.metadata.drop_all(db)
        pass

    def test_getting_all_projects(self):
        # HTTP GET request to the application on certain path
        prj = self.app.get('/projects')

        # assert the status code and type of response
        self.assertEqual(prj.status_code, 200)
        self.assertEqual(prj.content_type, 'application/json')
        # self.assertEqual(prj.data, b'{"message": "There are no projects"}\n')

    # Test data:
    # data = {
    #     'status': 'create_schema',
    #     'name': 'eugene',
    #     'contract_id': '18f441a0-d0b1-4b22-b16b-c1e718dab64d'
    # }

    # def test_posting_project(self):
    #     # HTTP POST request
    #     prj = self.app.post('/projects', data=None)
    #     # data = json.dumps(self.data), content_type = 'application/json'
    #     self.assertEqual(prj.content_type, 'application/json')
        # self.assertEqual(prj.status_code, 201)

    # def test_initialize_projects_post(self):
    #     # HTTP POST request with no data
    #     prj = self.app.post('/projects', data=None)
    #     self.assertEqual(prj.status_code, 201)

    # def test_getting_certain_project(self, _id='e3cb6cec-2945-4490-828d-f8267d925ca3'):
    #     # HTTP GET request to the application on certain path
    #     prj = self.app.get('/projects/{}'.format(_id))
    #     self.assertEqual(prj.status_code, 200)

    def test_getting_certain_project_denial(self, _id='00000000-0000-0000-0000-000000000000'):
        # HTTP GET request with incorrect id
        prj = self.app.get('/projects/{}'.format(_id))
        self.assertEqual(prj.status_code, 404)

    # def test_patching_certain_project(self, _id='e3cb6cec-2945-4490-828d-f8267d925ca3'):
    #     # HTTP PATCH request to the application on certain path
    #     prj = self.app.patch('/projects/{}'.format(_id))
    #     self.assertEqual(prj.status_code, 200)

    # def test_patching_certain_project_denial(self, _id='00000000-0000-0000-0000-000000000000'):
    #     # HTTP PATCH request with incorrect id
    #     prj = self.app.patch('/projects/{}'.format(_id))
    #     self.assertEqual(prj.status_code, 500)

    # def test_delete_certain_project(self, _id='e3cb6cec-2945-4490-828d-f8267d925ca3'):
    #     # HTTP DELETE request to the application on certain path
    #     prj = self.app.delete('/projects/{}'.format(_id))
    #     self.assertEqual(prj.status_code, 200)

    def test_deleting_certain_project_denial(self, _id='00000000-0000-0000-0000-000000000000'):
        # HTTP GET request with incorrect id
        prj = self.app.delete('/projects/{}'.format(_id))
        self.assertEqual(prj.status_code, 404)

    # def test_add(self):
    #     rv = self.app.get('/add/2/3')
    #     self.assertEqual(rv.status, '200 OK')
    #     self.assertEqual(rv.data, '5')
    #
    #     rv = self.app.get('/add/0/10')
    #     self.assertEqual(rv.status, '200 OK')
    #     self.assertEqual(rv.data, '10')
    #
    # def test_404(self):
    #     rv = self.app.get('/other')
    #     self.assertEqual(rv.status, '404 NOT FOUND')

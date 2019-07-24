# python -m unittest test_api to run tests

from flask import json
from .test_base import BaseTestCase


# Test data:
MOCK_PROJECT = {
            'status': 'create',
            'name': 'user_project',
            'contract_id': '93111111-aaaa-aaaa-aaaa-111111111110'}


class ProjectsInitializerTest(BaseTestCase):

    def test_getting_all_projects(self):
        with self.client:
            response = self.client.get("/projects/")
            self.assertEqual(response.content_type, 'application/json')
            self.assertEqual(response.status_code, 200)

    def test_creating_projects(self):
        with self.client:
            response = self.client.post("/projects/",
                                        data=json.dumps(MOCK_PROJECT),
                                        content_type='application/json')
            self.assertEqual(response.content_type, 'application/json')
            self.assertEqual(response.status_code, 201)

    def test_creating_projects_insufficient_data(self):
        with self.client:
            response = self.client.post('/projects/',
                                        data=json.dumps(MOCK_PROJECT.get('project_id')),
                                        content_type='application/json')
            self.assertEqual(json.loads(response.data), {'message': 'Insufficient project data'})
            self.assertEqual(response.status_code, 400)


class ProjectsIdTest(BaseTestCase):

    def test_getting_project_id_denial(self, _id='00000000-0000-0000-0000-000000000000'):
        with self.client:
            response = self.client.get('/projects/{}'.format(_id))
            self.assertEqual(response.content_type, 'application/json')
            self.assertEqual(json.loads(response.data), {'message': 'Project with this id does not exist'})
            self.assertEqual(response.status_code, 404)

    def test_patching_project_id_denial(self, _id='00000000-0000-0000-0000-000000000000'):
        with self.client:
            response = self.client.patch('/projects/{}'.format(_id),
                                         data=json.dumps(MOCK_PROJECT),
                                         content_type='application/json')
            self.assertEqual(response.content_type, 'application/json')
            self.assertEqual(json.loads(response.data), {'message': 'Project with this id does not exist'})
            self.assertEqual(response.status_code, 404)

    def test_deleting_project_id_denial(self, _id='00000000-0000-0000-0000-000000000000'):
        with self.client:
            response = self.client.delete('/projects/{}'.format(_id))
            self.assertEqual(response.content_type, 'application/json')
            self.assertEqual(json.loads(response.data), {'message': 'Project with this id does not exist'})
            self.assertEqual(response.status_code, 404)


class ProjectsDataResourcesTest(BaseTestCase):

    def test_posting_to_data_denial(self, _id='00000000-0000-0000-0000-000000000000'):
        with self.client:
            response = self.client.post('/projects/{}/data'.format(_id),
                                        data=json.dumps(MOCK_PROJECT),
                                        content_type='application/json')
            self.assertEqual(json.loads(response.data), {'message': 'Project with this id does not exist'})
            self.assertEqual(response.status_code, 404)


class StatusUpdateTest(BaseTestCase):

    def test_patching_project_id_denial(self, _id='00000000-0000-0000-0000-000000000000'):
        with self.client:
            response = self.client.patch('/projects/{}/status'.format(_id),
                                         data=json.dumps(MOCK_PROJECT),
                                         content_type='application/json')
            self.assertEqual(response.content_type, 'application/json')
            self.assertEqual(json.loads(response.data), {'message': 'Project with this id does not exist'})
            self.assertEqual(response.status_code, 404)


class CalculationDataTest(BaseTestCase):
    def test_all_calculation_data_denial(self, _id='00000000-0000-0000-0000-000000000000'):
        with self.client:
            response = self.client.get('/projects/{}/calculations'.format(_id))
            self.assertEqual(json.loads(response.data), {'message': 'Project with this id does not exist'})
            self.assertEqual(response.status_code, 404)

    def test_page_calculation_data_denial(self, _id='00000000-0000-0000-0000-000000000000', page=1):
        with self.client:
            response = self.client.get('/projects/{}/calculations/{page}'.format(_id, page=page))
            self.assertEqual(json.loads(response.data), {'message': 'Project with this id does not exist'})
            self.assertEqual(response.status_code, 404)

    def test_wrong_page_calculation(self, _id='00000000-0000-0000-0000-000000000000', page=0):
        with self.client:
            response = self.client.get('/projects/{}/calculations/{page}'.format(_id, page=page))
            self.assertEqual(json.loads(response.data), {'message': 'Project with this id does not exist'})
            self.assertEqual(response.status_code, 404)

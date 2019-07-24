# python -m unittest test_api to run tests

from flask import json
from .test_base import BaseTestCase


# Test data:
MOCK_DATA = {
            'status': 'create',
            'name': 'user_project',
            'contract_id': '71111111-aaaa-aaaa-aaaa-111111111111'
}


class ProjectsInitializerTest(BaseTestCase):

    def test_getting_all_projects(self):
        with self.client:
            response = self.client.get("/projects/")
            self.assertEqual(response.status_code, 200)
            self.assertEqual(response.content_type, 'application/json')

    # def test_posting_to_projects(self):
    #     with self.client:
    #         response = self.client.post("/projects/",
    #                                     data=json.dumps(MOCK_DATA),
    #                                     content_type='application/json')
    #         self.assertEqual(json.loads(response.data).get('project_id'), {'project_id': 'None'})
    #         self.assertEqual(response.status_code, 201)
    #         self.assertEqual(response.content_type, 'application/json')


class ProjectsIdTest(BaseTestCase):

    def test_getting_project_id_denial(self, _id='00000000-0000-0000-0000-000000000000'):
        with self.client:
            response = self.client.get('/projects/{}'.format(_id))
            self.assertEqual(response.content_type, 'application/json')
            self.assertEqual(json.loads(response.data), {'message': 'Project with this id does not exist'})
            self.assertEqual(response.status_code, 404)

    # def test_getting_project_by_id_success(self, _id='00000000-0000-0000-0000-000000000000'):
    #     with self.client:
    #         post = self.client.post("/projects/",
    #                                 data=json.dumps(MOCK_DATA),
    #                                 content_type='application/json')
    #         _id = json.loads(post.data).get('status')
    #         # response = self.client.get('/projects/{}'.format(_id))
    #         self.assertIs(type(_id), str)
    #         self.assertEqual(_id, 'create')
            # self.assertEqual(response.content_type, 'application/json')
            # self.assertEqual(response.status_code, 200)

    def test_patching_project_id_denial(self, _id='00000000-0000-0000-0000-000000000000'):
        with self.client:
            response = self.client.patch('/projects/{}'.format(_id),
                                         data=json.dumps(MOCK_DATA),
                                         content_type='application/json')
            self.assertEqual(response.content_type, 'application/json')
            self.assertEqual(json.loads(response.data), {'message': 'Project with this id does not exist'})
            self.assertEqual(response.status_code, 404)

    # def test_patching_project_by_id_success(self, _id='91c7f752-0ee7-405a-8523-1517a4059713'):
    #     with self.client:
    #         response = self.client.patch('/projects/{}'.format(_id), data=json.dumps(MOCK_DATA),
    #                                      content_type='application/json')
    #         self.assertEqual(response.content_type, 'application/json')
    #         self.assertEqual(response.status_code, 200)

    def test_deleting_project_id_denial(self, _id='00000000-0000-0000-0000-000000000000'):
        with self.client:
            response = self.client.delete('/projects/{}'.format(_id))
            self.assertEqual(response.content_type, 'application/json')
            self.assertEqual(json.loads(response.data), {'message': 'Project with this id does not exist'})
            self.assertEqual(response.status_code, 404)

    # def test_deleting_project_id_success(self, _id='00000000-0000-0000-0000-000000000000'):
    #     with self.client:
    #         response = self.client.delete('/projects/{}'.format(_id))
    #         self.assertEqual(response.content_type, 'application/json')
    #         # self.assertEqual(json.loads(response.data), {'message': 'Project with this id does not exist'})
    #         self.assertEqual(response.status_code, 404)


class ProjectsDataResourcesTest(BaseTestCase):

    def test_posting_to_data_denial(self, _id='00000000-0000-0000-0000-000000000000'):
        with self.client:
            response = self.client.post('/projects/{}/data'.format(_id),
                                        data=json.dumps(MOCK_DATA),
                                        content_type='application/json')
            self.assertEqual(json.loads(response.data), {'message': 'Project with this id does not exist'})
            self.assertEqual(response.status_code, 404)

    # def test_posting_to_data_success(self, _id='00000000-0000-0000-0000-000000000000'):
    #     with self.client:
    #         response = self.client.post('/projects/{}/data'.format(_id),
    #                                     data=json.dumps(MOCK_DATA),
    #                                     content_type='application/json')
    #         # self.assertEqual(json.loads(response.data), {'message': 'Project with this id does not exist'})
    #         self.assertEqual(response.status_code, 201)


class StatusUpdateTest(BaseTestCase):

    def test_patching_project_id_denial(self, _id='00000000-0000-0000-0000-000000000000'):
        with self.client:
            response = self.client.patch('/projects/{}/status'.format(_id),
                                         data=json.dumps(MOCK_DATA),
                                         content_type='application/json')
            self.assertEqual(response.content_type, 'application/json')
            self.assertEqual(json.loads(response.data), {'message': 'Project with this id does not exist'})
            self.assertEqual(response.status_code, 404)
#
#     # def test_patching_project_by_id_success(self, _id='00000000-0000-0000-0000-000000000000'):    #
#     #     with self.client:
#     #         response = self.client.patch('/projects/{}'.format(_id), data=json.dumps(MOCK_DATA),
#     #                                          content_type='text/html')
#     #         self.assertEqual(response.content_type, 'text/html')
#     #         self.assertEqual(response.status_code, 201)


class CalculationDataTest(BaseTestCase):
    def test_all_calculation_data_denial(self, _id='00000000-0000-0000-0000-000000000000'):
        with self.client:
            response = self.client.get('/projects/{}/calculations'.format(_id))
            self.assertEqual(json.loads(response.data), {'message': 'Project with this id does not exist'})
            self.assertEqual(response.status_code, 404)

    # def test_all_calculation_data_success(self, _id='00000000-0000-0000-0000-000000000000'):
    #     pass

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

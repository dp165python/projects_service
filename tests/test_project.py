# python -m unittest test_api to run tests

from flask import json
from .test_base import BaseTestCase


class ProjectsTest(BaseTestCase):

    # Test data:
    mock_data = {
                'status': 'create',
                'name': 'eugene',
                'contract_id': '31111111-aaaa-aaaa-aaaa-111111111110'
    }

    def test_getting_all_projects(self):
        with self.client:
            response = self.client.get("/projects")
            self.assertEqual(response.status_code, 200)
            self.assertEqual(response.content_type, 'application/json')

    def test_posting_to_projects(self):
        with self.client:
            response = self.client.post("/projects", data=json.dumps(self.mock_data),
                                        content_type='application/json')
            # self.assertEqual(response.status_code, 201)
            self.assertEqual(response.content_type, 'application/json')


class ProjectsIdTest(BaseTestCase):

    # Test data:
    mock_data = {
                'status': 'create',
                'name': 'user',
                'contract_id': '11111111-aaaa-aaaa-aaaa-111111111111'
    }

    def test_getting_project_id_denial(self, _id='00000000-0000-0000-0000-000000000000'):
        with self.client:
            response = self.client.get('/projects/{}'.format(_id))
            self.assertEqual(response.content_type, 'application/json')
            self.assertEqual(response.data, b'{"error": "Project doesn\'t exist"}\n')
            self.assertEqual(response.status_code, 404)

    # def test_getting_project_by_id_success(self, _id='00000000-0000-0000-0000-000000000000'):
    #     with self.client:
    #         response = self.client.get('/projects/{}'.format(_id))
    #         self.assertEqual(response.content_type, 'application/json')
    #         self.assertEqual(response.status_code, 200)

    def test_patching_project_id_denial(self, _id='00000000-0000-0000-0000-000000000000'):
        with self.client:
            response = self.client.patch('/projects/{}'.format(_id), data=json.dumps(self.mock_data),
                                         content_type='application/json')
            self.assertEqual(response.content_type, 'application/json')
            self.assertEqual(response.data, b'{"error": "Project doesn\'t exist"}\n')
            self.assertEqual(response.status_code, 404)

    # def test_patching_project_by_id_success(self, _id='00000000-0000-0000-0000-000000000000'):
    #     with self.client:
    #         response = self.client.patch('/projects/{}'.format(_id), data=json.dumps(self.mock_data),
    #                                          content_type='application/json')
    #         self.assertEqual(response.content_type, 'application/json')
    #         self.assertEqual(response.status_code, 200)

    def test_deleting_project_id_denial(self, _id='00000000-0000-0000-0000-000000000000'):
        with self.client:
            response = self.client.delete('/projects/{}'.format(_id))
            self.assertEqual(response.content_type, 'application/json')
            self.assertEqual(response.data, b'{"error": "Project doesn\'t exist"}\n')
            self.assertEqual(response.status_code, 404)

    # def test_deleting_project_id_success(self, _id='00000000-0000-0000-0000-000000000000'):
    #     with self.client:
    #         response = self.client.delete('/projects/{}'.format(_id))
    #         self.assertEqual(response.content_type, 'application/json')
    #         # self.assertEqual(response.data, b'{"error": "Project doesn\'t exist"}\n')
    #         self.assertEqual(response.status_code, 404)

    # def test_posting_to_projects(self):
    #     with self.client:
    #         response = self.client.post("/projects",
    #                                     data={"status": self.mock_data['status'],
    #                                           "name": "eugene",
    #                                           "contract_id": self.mock_data['contract_id']
    #                                           })
    #         self.assertEqual(response.status_code, 201)
    #         self.assertEqual(response.content_type, 'application/json')

    def test_getting_project_id_denial(self, _id='00000000-0000-0000-0000-000000000000'):
        with self.client:
            response = self.client.get('/projects/{}'.format(_id))
            self.assertEqual(response.content_type, 'application/json')
            self.assertEqual(response.data, b'{"error": "Project doesn\'t exist"}\n')
            self.assertEqual(response.status_code, 404)

    # def test_getting_project_by_id_success(self, _id='00000000-0000-0000-0000-000000000000'):
    #     with self.client:
    #         response = self.client.get('/projects/{}'.format(_id))
    #         self.assertEqual(response.content_type, 'application/json')
    #         self.assertEqual(response.status_code, 200)

    def test_patching_project_id_denial(self, _id='00000000-0000-0000-0000-000000000000'):
        with self.client:
            response = self.client.patch('/projects/{}'.format(_id), data=json.dumps(self.mock_data),
                                         content_type='application/json')
            self.assertEqual(response.content_type, 'application/json')
            self.assertEqual(response.data, b'{"error": "Project doesn\'t exist"}\n')
            self.assertEqual(response.status_code, 404)

    # def test_patching_project_by_id_success(self, _id='00000000-0000-0000-0000-000000000000'):
    #     with self.client:
    #         response = self.client.patch('/projects/{}'.format(_id), data=json.dumps(self.mock_data),
    #                                          content_type='application/json')
    #         self.assertEqual(response.content_type, 'application/json')
    #         self.assertEqual(response.status_code, 200)

    def test_deleting_project_id_denial(self, _id='00000000-0000-0000-0000-000000000000'):
        with self.client:
            response = self.client.delete('/projects/{}'.format(_id))
            self.assertEqual(response.content_type, 'application/json')
            self.assertEqual(response.data, b'{"error": "Project doesn\'t exist"}\n')
            self.assertEqual(response.status_code, 404)

    # def test_deleting_project_id_success(self, _id='00000000-0000-0000-0000-000000000000'):
    #     with self.client:
    #         response = self.client.delete('/projects/{}'.format(_id))
    #         self.assertEqual(response.content_type, 'application/json')
    #         # self.assertEqual(response.data, b'{"error": "Project doesn\'t exist"}\n')
    #         self.assertEqual(response.status_code, 404)

    def test_getting_project_id_denial(self, _id='00000000-0000-0000-0000-000000000000'):
        with self.client:
            response = self.client.get('/projects/{}'.format(_id))
            self.assertEqual(response.content_type, 'application/json')
            self.assertEqual(response.data, b'{"error": "Project doesn\'t exist"}\n')
            self.assertEqual(response.status_code, 404)

    # def test_getting_project_by_id_success(self, _id='00000000-0000-0000-0000-000000000000'):
    #     with self.client:
    #         response = self.client.get('/projects/{}'.format(_id))
    #         self.assertEqual(response.content_type, 'application/json')
    #         self.assertEqual(response.status_code, 200)

    def test_patching_project_id_denial(self, _id='00000000-0000-0000-0000-000000000000'):
        with self.client:
            response = self.client.patch('/projects/{}'.format(_id), data=json.dumps(self.mock_data),
                                         content_type='application/json')
            self.assertEqual(response.content_type, 'application/json')
            self.assertEqual(response.data, b'{"error": "Project doesn\'t exist"}\n')
            self.assertEqual(response.status_code, 404)

    # def test_patching_project_by_id_success(self, _id='00000000-0000-0000-0000-000000000000'):
    #     with self.client:
    #         response = self.client.patch('/projects/{}'.format(_id), data=json.dumps(self.mock_data),
    #                                          content_type='application/json')
    #         self.assertEqual(response.content_type, 'application/json')
    #         self.assertEqual(response.status_code, 200)

    def test_deleting_project_id_denial(self, _id='00000000-0000-0000-0000-000000000000'):
        with self.client:
            response = self.client.delete('/projects/{}'.format(_id))
            self.assertEqual(response.content_type, 'application/json')
            self.assertEqual(response.data, b'{"error": "Project doesn\'t exist"}\n')
            self.assertEqual(response.status_code, 404)

    # def test_deleting_project_id_success(self, _id='00000000-0000-0000-0000-000000000000'):
    #     with self.client:
    #         response = self.client.delete('/projects/{}'.format(_id))
    #         self.assertEqual(response.content_type, 'application/json')
    #         self.assertEqual(response.status_code, 201)


class DataHandlerTest(BaseTestCase):

    # Test data:
    mock_data = {
                'field_1': '777',
                'field_2': '333',
                'field_3': '3.1415',
                'field_4': '0',
                'field_5': 'Give us a decent job'
    }

    def test_posting_to_data_denial(self, _id='00000000-0000-0000-0000-000000000000'):
        with self.client:
            response = self.client.post('/projects/{}/data'.format(_id),
                                        data=json.dumps(self.mock_data),
                                        content_type='application/json')
            self.assertEqual(response.data, b'{"error": "Project doesn\'t exist"}\n')
            self.assertEqual(response.status_code, 404)

    # def test_posting_to_data_success(self, _id='00000000-0000-0000-0000-000000000000'):
    #     with self.client:
    #         response = self.client.post('/projects/{}/data'.format(_id),
    #                                     data=json.dumps(self.mock_data),
    #                                     content_type='application/json')
    #         # self.assertEqual(response.data, b'{"error": "Project doesn\'t exist"}\n')
    #         self.assertEqual(response.status_code, 201)


class StatusUpdateTest(BaseTestCase):

    # Test data:
    mock_data = {
        'status': 'updated',
        'contract_id': '11111111-aaaa-aaaa-aaaa-111111111111'
    }

    def test_patching_project_id_denial(self, _id='00000000-0000-0000-0000-000000000000'):
        with self.client:
            response = self.client.patch('/projects/{}/status'.format(_id), data=json.dumps(self.mock_data),
                                         content_type='application/json')
            self.assertEqual(response.content_type, 'application/json')
            self.assertEqual(response.data, b'{"error": "Project doesn\'t exist"}\n')
            self.assertEqual(response.status_code, 404)

    # def test_patching_project_by_id_success(self, _id='00000000-0000-0000-0000-000000000000'):    #
    #     with self.client:
    #         response = self.client.patch('/projects/{}'.format(_id), data=json.dumps(self.mock_data),
    #                                          content_type='application/json')
    #         self.assertEqual(response.content_type, 'application/json')
    #         self.assertEqual(response.status_code, 201)


class CalculationDataTest(BaseTestCase):

    def test_all_calculation_data_denial(self, _id='00000000-0000-0000-0000-000000000000'):
        with self.client:
            response = self.client.get('/projects/{}/calculations'.format(_id))
            self.assertEqual(response.data, b'{"error": "Project doesn\'t exist"}\n')
            self.assertEqual(response.status_code, 404)

    # def test_all_calculation_data_success(self, _id='00000000-0000-0000-0000-000000000000'):
    #     pass

    def test_page_calculation_data_denial(self, _id='00000000-0000-0000-0000-000000000000', page=1):
        with self.client:
            response = self.client.get('/projects/{}/calculations/{page}'.format(_id, page=page))
            self.assertEqual(response.data, b'{"error": "Project doesn\'t exist"}\n')
            self.assertEqual(response.status_code, 404)
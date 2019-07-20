from http import HTTPStatus

from tests.test_base import BaseTestCase


# class TestSmoke(BaseTestCase):
#
#     def test_projects(self):
#         response = self.projects.get("/mono-statistics/smoke")
#         self.assertEqual(response.status_code, HTTPStatus.OK)
#         self.assertEqual(response.json["status"], "success")
#         self.assertEqual(response.json["message"], "ok")
#         self.assertIn("response_datetime", response.json.keys())


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
            # response = self.client.post("/projects", data=json.dumps(self.mock_data),
                                        content_type='application/json')
            # self.assertEqual(response.status_code, 201)
            self.assertEqual(response.content_type, 'application/json')
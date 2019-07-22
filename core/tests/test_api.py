import os
import pytest
import unittest

from core.app import app
from core.connector import create_database, drop_database


class TestApi(unittest.TestCase):
    def setUp(self) -> None:
        self.client = app.test_client()

        with app.app_context():
            print(os.getenv("APP_ENV"))
            app.config['DB_NAME'] = 'projects_test'
            create_database()

    def test_get(self):
        response = self.client.get('/projects/')
        print(response.data)

    # def tearDown(self) -> None:
        # with app.app_context():
        #     drop_database()

import json
import os
import pytest
import unittest

from flask import g, jsonify

from core.app import app
from core.connector import create_database, drop_database


def db_worker(mode):
    with app.app_context():
        if mode == 'init':
            app.config['DB_NAME'] = 'projects_test'
            create_database()
        elif mode == 'drop':
            drop_database()


class TestApi(unittest.TestCase):
    def setUp(self) -> None:
        self.client = app.test_client()
        app.config['DB_NAME'] = 'projects_test'
        with app.app_context():
            create_database()

    def test_get(self):
        response = self.client.get('/projects/')
        print(json.loads(response.data))

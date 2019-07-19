from flask_testing import TestCase

from core.app import app
from core.config import TestConfig
from core.connector import create_database, drop_database


class BaseTestCase(TestCase):
    """A base test case for projects_service"""

    def create_app(self):
        app.config.from_object(TestConfig)
        return app

    def setUp(self):
        create_database('test_api')
        # self.app = self.create_app()
        # self.app_context = self.app.app_context()
        # self.app_context.push()
        # db.create_all()

    def tearDown(self):
        # db.session.remove()
        # db.drop_all()
        drop_database('test_api')

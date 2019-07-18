from flask_testing import TestCase

from core.app import app
from core.config import db, TestConfiguration


class BaseTestCase(TestCase):
    """A base test case for projects_service"""

    def create_app(self):
        app.config.from_object(TestConfiguration)
        return app

    def setUp(self):
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

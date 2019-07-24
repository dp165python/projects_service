from flask_testing import TestCase
from flask import Flask
from core.app import app
from core.config import TestConfig
from core.connector import create_database, drop_database, create_engine
from flask_sqlalchemy import SQLAlchemy


class BaseTestCase(TestCase):
    """A base test case for projects_service"""

    def create_app(self):
        app = Flask(__name__)
        app.config['TESTING'] = True
        app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://eugene:1401@localhost/test_api'
        return app

    def setUp(self):
        self.client = app.test_client()
        app.config['DB_NAME'] = 'test_api'
        with app.app_context():
            create_database()

    # def tearDown(self):
    #     # db.session.remove()
    #     db.drop_all()
    #     # drop_database('test_api')
    #     db.init_app(self.app)
    #     with self.app.app_context():
    #         db.drop_all()

from flask_testing import TestCase
from flask import Flask
from core.app import app
from core.config import TestConfig
from core.connector import create_database, drop_database, create_engine
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class BaseTestCase(TestCase):
    """A base test case for projects_service"""

    def create_app(self):
        app = Flask(__name__)
        app.config['TESTING'] = True
        app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://eugene:1401@localhost/test_api'
        # app.config.from_object(TestConfig)
        db.init_app(app)
        app.app_context().push()  # this does the binding
        return app

    # def setUp(self):
    #     self.app = app.test_client
    #     with app.app_context():
    #         # self.session = create_engine(get_db_uri() + '_test').connect()
    #         global db
    #         db = create_engine('postgresql://eugene:1401@localhost/test_api').connect()
    #         db.create_all()
    #         create_database('test_api')
    #
    def setUp(self):
        # db = create_engine('postgresql://eugene:1401@localhost/test_api').connect()
        # self.app = self.create_app()
        # self.app_context = self.app.app_context()
        self.app = app.test_client()
        db.drop_all()
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()
    #     # drop_database('test_api')
    #     db.init_app(self.app)
    #     with self.app.app_context():
    #         db.drop_all()

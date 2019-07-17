from flask_testing import TestCase
from core.app import app
from core.config import db


class BaseTestCase(TestCase):
    """A base test case for projects_service"""

    SQLALCHEMY_DATABASE_URI = 'postgresql://eugene:1401@localhost/test_api'
    TESTING = True

    def create_app(self):
        # app.config['SQLALCHEMY_DATABASE_URI']
        app.config.from_object('core.config.TestConfiguration')
        # with app.app_context():
        #     db.init_app(app)
        #     migrate.init_app(app, db)
        return app

    def setUp(self):
        db.create_all()
        # db.session.commit()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

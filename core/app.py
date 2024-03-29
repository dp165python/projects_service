from flask import Flask, g
from flask_restful import Api
from sqlalchemy.orm import sessionmaker

from core.config import runtime_config
from core.connector import get_connection
from core.resources.projects_resources import ProjectsInitializer, ProjectsResources, ProjectsStatusUpdater, \
    ProjectsDataResources

from core.resources.projects_calculation import ProjectsDataToCalculation, ProjectsDataToCalculationPage
from core.utils.custom_response import MyResponse

app = Flask(__name__)
app.config.from_object(runtime_config())
app.response_class = MyResponse


@app.before_request
def open_session():
    g.conn = get_connection()
    session = sessionmaker()
    session.configure(bind=g.conn)
    g.session = session()


@app.teardown_request
def close_session(e):
    if 'session' in g:
        if e is None:
            g.session.commit()
        else:
            g.session.rollback()

        g.session.close()
        g.session = None


api = Api(app, prefix='/projects')

api.add_resource(ProjectsInitializer, '/')
api.add_resource(ProjectsResources, '/<id>')

api.add_resource(ProjectsDataResources, '/<id>/data')
api.add_resource(ProjectsStatusUpdater, '/<id>/status')

api.add_resource(ProjectsDataToCalculation, '/<id>/calculations')
api.add_resource(ProjectsDataToCalculationPage, '/<id>/calculations/<int:page_num>')

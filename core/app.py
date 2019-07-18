from flask import Flask, g
from flask_restful import Api
from sqlalchemy.orm import sessionmaker

from core.config import runtime_config
from core.connector import get_connection
from core.resources.projects_resources import ProjectsInitializer, ProjectsResources
# from core.resources.projects_resources import ProjectsResources
#
# from core.resources.status_updater import StatusUpdater
# from core.resources.data_handler import DataHandler
#
# from core.resources.projects_calculation import ProjectsCalculation
# from core.resources.projects_calculation_page import ProjectsCalculationPage
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
#
# api.add_resource(DataHandler, '/<id>/data')
# api.add_resource(StatusUpdater, '/<id>/status')
#
# api.add_resource(ProjectsCalculation, '/<id>/calculations')
# api.add_resource(ProjectsCalculationPage, '/<id>/calculations/<int:page_num>')

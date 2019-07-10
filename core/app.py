from core.config import create_app
from core.api import api_blueprint, api

from core.resources.projects_initializer import ProjectsInitializer
from core.resources.projects_resources import ProjectsResources

from core.resources.status_updater import StatusUpdater
from core.resources.data_handler import DataHandler

from core.resources.projects_calculation import ProjectsCalculation
from core.resources.projects_calculation_page import ProjectsCalculationPage


app = create_app()
app.register_blueprint(api_blueprint)

api.add_resource(ProjectsInitializer, '/projects')
api.add_resource(ProjectsResources, '/projects/<id>')

api.add_resource(DataHandler, '/projects/<id>/data')
api.add_resource(StatusUpdater, '/projects/<id>/status')

api.add_resource(ProjectsCalculation, '/projects/<id>/calculations')
api.add_resource(ProjectsCalculationPage, '/projects/<id>/calculations/<int:page_num>')

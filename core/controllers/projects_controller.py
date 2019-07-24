import uuid

from flask import g, abort
from core.models.models import Projects, Data


class ProjectsController:

    def get_projects(self):
        projects = g.session.query(Projects).all()
        return projects

    def get_project_by_id(self, id):
        project = g.session.query(Projects).filter(Projects.id == id).first()
        if not project:
            abort(404, 'Project with this id does not exist')
        return project

    def create_project(self, data, errors):
        if errors:
            abort(404, errors)
        elif len(data) < 3:
            abort(400, 'Insufficient project data')

        project_name = data['name']
        contract_id = data['contract_id']
        project = Projects(name=project_name, contract_id=contract_id, status='default')
        g.session.add(project)
        return g.session.query(Projects).filter(Projects.contract_id == contract_id).first()

    def delete_project(self, id):
        deleted_project = g.session.query(Projects).filter(Projects.id == id).first()

        if not deleted_project:
            abort(404, 'Project with this id does not exist')
        g.session.query(Projects).filter(Projects.id == id).delete()
        return deleted_project

    def update_contract_id(self, id, data, errors):
        if errors:
            abort(404, errors)

        contract_id = data['contract_id']
        project = g.session.query(Projects).filter(Projects.id == id).first()

        if not project:
            abort(404, 'Project with this id does not exist')

        project.contract_id = contract_id
        return project

    def update_project_status(self, id, data, errors):
        if errors:
            abort(404, errors)

        status = data['status']
        project = g.session.query(Projects).filter(Projects.id == id).first()

        if not project:
            abort(404, 'Project with this id does not exist')

        project.status = status
        return project

    def save_projects_data(self, id, data, errors):
        if errors:
            abort(404, errors)

        if not g.session.query(Projects).filter(Projects.id == id).first():
            abort(404, 'Project with this id does not exist')

        if len(data['data']) < 5:
            abort(400, 'Incorrect data loaded')

        data_length = 0
        for data in data['data']:
            project_data = Data(
                project_id=uuid.UUID(id),
                field_1=data['field_1'],
                field_2=data['field_2'],
                field_3=data['field_3'],
                field_4=data['field_4'],
                field_5=data['field_5'],
            )

            data_length += 1
            g.session.add(project_data)
        return data_length


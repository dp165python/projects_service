class ProjectData:
    def __init__(self, project):
        self._project = project

    def transform_project_data_into_dict(self):
        return {
            'project_id': str(self._project.id),
            'contract_id': str(self._project.contract_id),
            'name': self._project.name,
            'status': self._project.status
        }

class Data:
    def __init__(self, data):
        self._data = data

    def transform_data_into_dict(self):
        return {
            'field_1': self._data[0].field_1,
            'field_2': self._data[0].field_2,
            'field_3': self._data[0].field_3,
            'field_4': self._data[0].field_4,
            'field_5': self._data[0].field_5
        }

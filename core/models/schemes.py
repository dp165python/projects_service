from marshmallow import Schema, fields


class StatusSchema(Schema):
    status = fields.Str(required=True)


class ContractIdSchema(Schema):
    contract_id = fields.Str(required=True)


class ProjectSchema(Schema):
    id = fields.Str()
    status = fields.Str()
    name = fields.Str(required=True)
    contract_id = fields.UUID(required=True)


class DataNestedSchema(Schema):
    field_1 = fields.Integer()
    field_2 = fields.Integer()
    field_3 = fields.Float()
    field_4 = fields.Integer()
    field_5 = fields.Str()


class DataSchema(Schema):
    data = fields.Nested(DataNestedSchema, many=True)

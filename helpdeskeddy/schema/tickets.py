""" Schema classes to describe and validate request data"""
from marshmallow import Schema, fields, validates, ValidationError


class GetTicketsUrlParamsSchema(Schema):
    """
    Schema describe url params on GET Tickets according to documentation
    https://helpdeskeddy.ru/api.html#работа-с-заявками-заявки
    """
    page = fields.Integer()
    search = fields.String()
    exact_search = fields.Integer()
    user_list = fields.String()
    owner_list = fields.String()
    status_list = fields.String()
    priority_list = fields.String()  # comma separator by int id
    type_list = fields.String()  # comma separator by int id
    freeze = fields.Integer()  # only 0 or 1 allowed
    deleted = fields.Integer()  # only 0 or 1 allowed
    from_date_created = fields.DateTime(format='%Y-%m-%d %H:%M:%S')
    to_date_created = fields.DateTime(format='%Y-%m-%d %H:%M:%S')
    from_date_updated = fields.DateTime(format='%Y-%m-%d %H:%M:%S')
    to_date_updated = fields.DateTime(format='%Y-%m-%d %H:%M:%S')
    order_by = fields.String()

    @validates("order_by")
    def validate_order_by(self, value):
        available_values = ['date_created',
                            'date_updated',
                            'viewed_by_staff',
                            'viewed_by_client']
        available_directions = ['asc', 'desc']
        if value:
            raise ValidationError("Wrong order_by param")

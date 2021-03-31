from marshmallow import Schema, fields, validates, ValidationError
from ..utils.abstract import Resource


class GetTicketsUrlParamsSchema(Schema):
    """
    Schema describe url params on GET Tickets according to documentation
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
        # date_created{desc}
        available_values = ['date_created',
                            'date_updated',
                            'viewed_by_staff',
                            'viewed_by_client']
        available_directions = ['asc', 'desc']
        if value:
            raise ValidationError("Wrong order_by param")


class TicketObject(Schema):
    # число (необязательный) Пример: 23
    # ID родительской заявки
    pid = fields.Int()

    # строка (обязательный) Пример: Problem with email
    # Название заявки
    title = fields.String()

    # строка (обязательный) Пример: <p>Problem with email info@example.com</p>
    # Текст заявки
    description = fields.String()

    # дата (необязательный) Пример: 01.01.1970 00:00
    # Дата и время SLA
    sla_date = fields.DateTime(format='%Y-%m-%d %H:%M:%S')

    # дата (необязательный) Пример: 01.01.1970 00:00
    # Заморозка заявки до даты и времени
    freeze_date = fields.DateTime(format='%Y-%m-%d %H:%M:%S')

    # строка (необязательный) Пример: process
    # Статус заявки
    status_id = fields.String()

    # число (необязательный) Пример: 1
    # ID приоритета
    priority_id = fields.String()

    # число (необязательный) Пример: 2
    # ID типа
    type_id = fields.String()

    # число (необязательный) Пример: 1
    # ID департамента
    department_id = fields.String()

    # булево (необязательный) Пример: false
    # Блокировка заявки. true - блокировать заявку. false - разблокировать заявку.
    ticket_lock = fields.String()

    # число (необязательный) Пример: 1
    # ID исполнителя
    owner_id = fields.String()

    # число (необязательный) Пример: 2
    # ID владельца заявки
    user_id = fields.String()

    # число (необязательный) Пример: email@example.com
    # Если не задан ID владельца заявки, то для создания заявки будет использоваться э-почта пользователя, если пользователь не существует, то он будет автоматически создан
    user_email = fields.String()

    # массив почтовых ящиков (необязательный)
    # Копия письма
    cc = fields.String()

    # массив почтовых ящиков (необязательный)
    # Скрытая копия письма
    bcc = fields.String()

    # массив user_id (необязательный)
    # Список пользователей следящих за заявкой, пользователь должен быть сотрудником.
    followers = fields.String()

    # число (необязательный) Пример: 1
    # Первый ответ в заявке от имени сотрудника – 0, от имени пользователя 1, по умолчанию 1
    create_from_user = fields.String()

    # массив (необязательный) Пример: [1 => 3, 2 => 0]
    # Массив индивидуальных полей заявки, пример: custom_fields[field_id] = value, в случае иерархического поля, необходимо указывать уровень custom_fields[field_id][level] = value
    custom_fields = fields.String()

    # массив файлов (необязательный)
    # Массив приложений
    files = fields.List(fields.Raw())


class Tickets(Resource):

    RESOURCE_ROOT = '/tickets/'

    def __init__(self, client=None):
        self.client = client

    def get(self, query=None):

        if query:
            if isinstance(query, dict):
                """Filter tickets via url params"""
                try:
                    result = GetTicketsUrlParamsSchema().load(query)
                    params = self.client.to_url_params(result)
                    return self.client.get(self.RESOURCE_ROOT + '?' + params)
                except ValidationError as e:
                    # TODO: exceptions
                    raise e.messages
                    # print(e.messages)
                    # print(e.valid_data)

            if isinstance(query, int):
                """Get single ticket by ID"""
                return self.client.get(self.RESOURCE_ROOT + str(query))

        return self.client.get(self.RESOURCE_ROOT)

    def post(self, data):
        try:
            validated_data = TicketObject().load(data)

            # Preapare incomming data to POST
            postdata = {}
            idx = 0
            # read request data
            for k in validated_data.keys():
                if k == 'files':
                    for f in validated_data['files']:
                        # if key starts with "files"
                        # TODO: check maximum size if needed ( use **options )
                        content_type = self.client.get_mime_type(f)

                        postdata[f'files[{idx}]'] = (
                            f.name,  # file name
                            f,  # file object
                            content_type
                        )
                        idx += 1
                else:
                    postdata[k] = str(validated_data[k])

            return self.client.post(self.RESOURCE_ROOT, postdata)
        except ValidationError as e:
            # TODO: exceptions
            raise e.messages

    def put(self):
        pass

    def delete(self):
        pass

import faker
import requests
import json
from data import URL



def base_method_post_serialize(endpoint, payload):
    response = requests.post(f'{URL}{endpoint}', json.dumps(payload))
    return response

def fake_data_order():
    fake = faker.Faker('ru_Ru')
    order = {
        "firstName": f'{fake.first_name()[0:10]}',
        "lastName": f'{fake.last_name()[0:10]}',
        "address": f'{fake.street_address()[0:20].replace('/', '')}',
        "metroStation": f'{fake.random_int(1,5)}',
        "phone": f'{fake.phone_number()}',
        "rentTime": f'{fake.random_int(1,5)}',
        "deliveryDate": f'{fake.date_between_dates()}',
        "comment": f'Для "{fake.name()}"',
        "color": []
    }
    return order




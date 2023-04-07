import json
from random import randint


def read_json_file(filename):
    with open(filename) as file:
        data = json.load(file)
    return data


def generate_new_command_values():
    command_name = f'new_{randint(999, 9999)}'
    description = f'Test Command_{randint(999, 9999)}'
    name_on_device = f'{command_name}_x'
    print(f'New command : {command_name}:{description}:{name_on_device}')
    return {'name': command_name, 'description': description, 'name_on_device': name_on_device}

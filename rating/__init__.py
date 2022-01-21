import json


def get_database_config() -> dict:
    with open("./config/config.txt") as file:
        file = file.read()
        return json.loads(file)

import json
def load_choices_from_json(file_path, id_key, name_key):
    with open(file_path, 'r', encoding="utf-8") as file:
        data = json.load(file)
        choices = [(item[id_key], item[name_key]) for item in data]
    return choices



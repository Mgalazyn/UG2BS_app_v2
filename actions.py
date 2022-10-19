import json


def add_exercise_to_accessory(new_data, filename='data_exercises/accesory_exercises.json'):
    with open(filename, 'r+') as f:
        file_data = json.load(f)
        file_data["accesory_exercises"].append(new_data)
        f.seek(0)
        json.dump(file_data, f, indent=4)


y = {f"Name": 'OHP', "Version": 'WIDE GRIP'}

add_exercise_to_accessory(y)

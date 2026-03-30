import json
import data

def save_json():
    try:
        with open('db.json', "w") as file:
            json.dump(data.student_database, file, indent=4)
        return True
    except:
        return False

def import_json():
    try:
        with open('db.json', "r") as file:
            data = json.load(file)
        return data
    except:
        return False
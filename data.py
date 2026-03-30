student_database = [
    {
        "id" : 1,
        "name" : "example_name",
        "age" : 6,
        "program" : "example_program",
        "status": "active"
    }
]

def register_student(name, age, program, status):
    try:
        student_id = len(student_database)+1
        student_array = {
            "id" : student_id,
            "name" : name, 
            "age" : age,
            "program" : program,
            "status" : status 
        }

        student_database.append(student_array)
        return True
    except:
        print("[x] error to register student")
        return False
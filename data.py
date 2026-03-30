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
        student_id = len(student_database)
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

def list_students():
    try:
        if len(student_database) == 1:
            print("[x] The database is empty.")
        else:
            print("----------Students list----------")
            for i in student_database:
                if i.get("name") == "example_name":
                    pass
                else:
                    print(f"\nID: {i.get("id")} \nName: {i.get("name")} \nAge: {i.get("age")} \nProgram: {i.get("program")} \nStatus: {i.get("status")}")
    except:
        print("[x] error to list students")

def search_student(key, student_info):
    search_list = []
    try:
        if key == 1:
            for item in student_database:
                name = item.get("id")
                if name == student_info:
                    search_list.append(item)
        elif key == 2:
            for item in student_database:
                name = item.get("name")
                if name == student_info:
                    search_list.append(item)
        elif key == 3:
            for item in student_database:
                name = item.get("age")
                if name == student_info:
                    search_list.append(item)
        elif key == 4:
            for item in student_database:
                name = item.get("program")
                if name == student_info:
                    search_list.append(item)
        elif key == 5:
            for item in student_database:
                name = item.get("status")
                if name == student_info:
                    search_list.append(item)
                    
        print("----------Students list----------")          
        for i in search_list:
            if i.get("name") == "example_name":
                pass
            else:
                print(f"\nID: {i.get("id")} \nName: {i.get("name")} \nAge: {i.get("age")} \nProgram: {i.get("program")} \nStatus: {i.get("status")}")
        
    except:
        print("[x] Error to search students")
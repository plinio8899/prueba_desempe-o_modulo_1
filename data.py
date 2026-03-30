#database schema
student_database = [
    {
        "id" : 0,
        "name" : "example_name",
        "age" : 6,
        "program" : "example_program",
        "status": "active"
    }
]

#register user in the schema
def register_student(name, age, program, status):
    try:
        #create a secuencial id
        student_id = len(student_database)
        #verify id
        for i in student_database:
            idd = i.get("id")
            #change the id if it already exists
            if idd == student_id:
                student_id = student_id + 1
        student_array = {
            "id" : student_id,
            "name" : name, 
            "age" : age,
            "program" : program,
            "status" : status 
        }
        #add on database
        student_database.append(student_array)
        return True
    except:
        print("[x] error to register student")
        return False

#list students function
def list_students():
    try:
        #ff only the example item is present, it is treated as empty.
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

#search function: Use `view` to decide whether to display the result in the console and use key and student to reference key and value
def search_student(key, student_info, view=True):
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
        if view:
            print("----------Students list----------")          
            for i in search_list:
                if i.get("name") == "example_name":
                    pass
                else:
                    print(f"\nID: {i.get("id")} \nName: {i.get("name")} \nAge: {i.get("age")} \nProgram: {i.get("program")} \nStatus: {i.get("status")}")
        else:
            return search_list
        
    except:
        print("[x] Error to search students")


def update_student(id, values):
    try:
        student = search_student(1, id, False)
        student_id = student[0].get("id")
        student_database[student_id]["name"] = values["name"]
        student_database[student_id]["age"] = values["age"]
        student_database[student_id]["program"] = values["program"]
        student_database[student_id]["status"] = values["status"]
        return True
    except:
        print("[x] invalid data: error to update datebase")


def delete_student(id):
    try:
        student = search_student(1, id, False)
        student_id = student[0].get("id")    
        student_database.pop(student_id)
    except:
        print("[x] invalid data: error to delete student")
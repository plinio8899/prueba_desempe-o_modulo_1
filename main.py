import os
import time
import data
inter = True

while inter:
    os.system("clear")
    print("----------student management----------")
    print("options:")
    print("1. Register student")
    print("2. Consult datebase")
    print("3. Search student")
    print("4. Update student information")
    print("5. Delete student")
    print("6. Exit")

    try:
        option = int(input("select option -> "))

        if option == 1:
            inter_register = True
            while inter_register:
                os.system("clear")
                try:
                    name = input("Insert full name (str) -> ")
                    age = int(input("Insert age (int) -> "))
                    program = input("Insert program name -> ")
                    status = int(input("Choice status (active = 0, inactive = 1 (please insert a int)) -> "))


                    if status != 0 and status != 1:
                        status = "inactive"
                        reg = data.register_student(name, age, program, status)
                        os.system("clear")
                        print("[?] The assigned state does not exist, we will assign the default inactive state.")
                        time.sleep(1)
                    else:
                        status = "active"
                        reg = data.register_student(name, age, program, status)

                    if not reg:
                        os.system("clear")
                        print("[x] Error to save student in the database")
                        time.sleep(1)
                    inter_register = False

                except:
                    os.system("clear")
                    print("[x] Error: invalid data")
                    time.sleep(1)
        elif option == 2:
            os.system("clear")
            data.list_students()
            input("\npress enter to continue...")
        elif option == 3:
            inter_search = True
            while inter_search:
                os.system("clear")
                print("----------Search by----------")
                print("1. ID")
                print("2. Name")
                print("3. Age")
                print("4. Program")
                print("5. Status")
                print("6. back")
                option_search = int(input("Choice option -> "))
                if option_search == 1:
                    try:
                        student_info = int(input("insert id -> "))
                        os.system("clear")
                        data.search_student(1, student_info)
                        input("Press enter to continue")
                    except:
                        print("[x] Error: invalid id")
                elif option_search == 2:
                    try:
                        student_info = input("insert name -> ")
                        os.system("clear")
                        data.search_student(2, student_info)
                        input("Press enter to continue")
                    except:
                        print("[x] Error: invalid name")
                elif option_search == 3:
                    try:
                        student_info = int(input("insert age -> "))
                        os.system("clear")
                        data.search_student(3, student_info)
                        input("Press enter to continue")
                    except:
                        print("[x] Error: invalid age")
                elif option_search == 4:
                    try:
                        student_info = input("insert program name -> ")
                        os.system("clear")
                        data.search_student(4, student_info)
                        input("Press enter to continue")
                    except:
                        print("[x] Error: invalid program name")
                elif option_search == 5:
                    try:
                        student_info = input("insert status (active or inactive) -> ")
                        os.system("clear")
                        data.search_student(5, student_info)
                        input("Press enter to continue")
                    except:
                        print("[x] Error: invalid status")
                elif option_search == 6:
                    inter_search = False
                else:
                    print("[x] Error: invalid option")
        elif option == 4:
            try:
                student_id = int(input("insert student ID -> "))
                inter_update = True
                while inter_update:
                    os.system("clear")
                    try:
                        data.search_student(1, student_id)
                        print("")
                        name = input("Insert full name (str) -> ")
                        age = int(input("Insert age (int) -> "))
                        program = input("Insert program name -> ")
                        status = int(input("Choice status (active = 0, inactive = 1 (please insert a int)) -> "))

                        values = {
                            "name" : name,
                            "age" : age,
                            "program" : program,
                            "status" : status
                        }

                        if status != 0 and status != 1:
                            status = "inactive"
                            reg = data.update_student(student_id, values)
                            os.system("clear")
                            print("[?] The assigned state does not exist, we will assign the default inactive state.")
                            time.sleep(1)
                        else:
                            status = "active"
                            reg = data.update_student(student_id, values)

                        if not reg:
                            os.system("clear")
                            print("[x] Error to update student in the database")
                            time.sleep(1)
                        inter_update = False

                    except:
                        os.system("clear")
                        print("[x] Error: invalid data")
                        time.sleep(1)
            except:
                print("[x] Error to update")
        elif option == 5:
            inter_delete = True
            while inter_delete:
                try:
                    student_id = int(input("insert student ID -> "))
                    data.delete_student(student_id)
                    os.system("clear")
                    print("[+] student deleted")
                    time.sleep(1)
                    inter_delete = False
                except:
                    print("[x] invalid ID")
        elif option == 6:
            inter = False
        else:
            os.system("clear")
            print("[x] choice a valid option")
            time.sleep(1)
    except:
        os.system("clear")
        print("[x] choice a valid option")
        time.sleep(1)
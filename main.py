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
    print("3. Search student by id")
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
                        status = 1
                        reg = data.register_student(name, age, program, status)
                        os.system("clear")
                        print("[?] The assigned state does not exist, we will assign the default inactive state.")
                        time.sleep(1)
                    else:
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
            print("consult")
        elif option == 3:
            print("search")
        elif option == 4:
            print("update")
        elif option == 5:
            print("delete")
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
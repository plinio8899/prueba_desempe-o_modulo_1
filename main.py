import os
import time
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
            print("register")
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
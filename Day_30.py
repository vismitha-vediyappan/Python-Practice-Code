#STUDENT MANAGEMENT SYSTEM (MINI PROJECT)

#create a students detail with dictionaries
student1 = { "name": "vismitha", "age": 21 ,"branch" : "ece","marks" :95}
student2 = { "name": "jk", "age": 22 ,"branch" : "cse","marks" :90}
student3 = { "name": "v", "age": 21 ,"branch" : "cse","marks" :90}

students = [student1 ,student2,student3]#dictories stored in list

#1.Add student
def add_student():
    user_student = {"name": input("enter name:"),
                    "age": int(input("enter age:")),
                    "branch": input("enter branch:"),
                    "marks": int(input("enter mark:"))
    }
    students.append(user_student)
add_student()

#2.View student
def view_students():
    for view in students :
        print( "----------------------" )
        for keys,values in view.items():
            print(f"{keys}:{values}")
view_students()

#3.Search student
def search_students():
    search_name = input("enter name:")
    found = False
    for search in students :
        if search_name == search.get("name"):
            print(search)
            found = True
    if found == False:
        print("student not found")
search_students()

#4.Update student
def update_students():
    update_name = input("enter name:")
    found = False
    for update in students :
        if update_name == update.get("name"):
            print(update)
            update["age"] =  int(input("enter age:"))
            update["branch"] = input("enter branch:")
            update["marks"] = int(input("enter mark:"))
            found = True
    if found == False:
        print("student not found")
update_students()

#5.Delete student
def delete_students():
    delete_name = input("enter name:")
    found = False
    for delete in students:
        if delete_name == delete.get("name"):
            print(delete)
            students.remove(delete)
            found = True
    if found == False:
        print("student not found")

#EXIT
while True:
    print ("1.Add Student")
    print("2.view students")
    print("3.search student")
    print("4.update student")
    print("5.delete student")
    print("6.EXIT")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_student()
    elif choice == "2":
        view_students()
    elif choice == "3":
        search_students()
    elif choice == "4" :
        update_students()
    elif choice == "5":
        delete_students()
    elif choice == "6":
        print("exit")
        break
    else:
        print("Invalid choice")















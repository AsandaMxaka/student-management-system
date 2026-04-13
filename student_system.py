students = []

def add_student():
    name = input("Enter student name: ")
    age = int(input("Enter student age: "))
    students.append({"name" : name, "age": age})
    print("Student added successfully!\n")

def view_students():
    if not students:
        print("No students found\n")
    else:
        for i, student in enumerate(students, start=1):
            print(f"{i}. Name: {student['name']}, Age: {student['age']}")
    

def menu():
    while True:
        print("=======STUDENT MANAGEMENT SYSTEM=========")
        print("1.Add student")
        print("2.View students")
        print("3.Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            add_student()
        elif choice == "2":
            view_students()
        elif choice == "3":
            print("Goodbye")
            break
        else:
            print("Invalid choice. Try again.\n")

menu()                        
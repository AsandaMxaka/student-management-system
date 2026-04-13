import sqlite3

# Connect to database (it will create file automatically)
conn = sqlite3.connect("students.db")
cursor = conn.cursor()

# Create table
cursor.execute("""
CREATE TABLE IF NOT EXISTS students (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    age INTEGER NOT NULL
)
""")

conn.commit()


def add_student():
    name = input("Enter student name: ")
    age = int(input("Enter student age: "))

    cursor.execute("INSERT INTO students (name, age) VALUES (?, ?)", (name, age))
    conn.commit()

    print("Student added successfully!\n")


def view_students():
    cursor.execute("SELECT * FROM students")
    rows = cursor.fetchall()

    if not rows:
        print("No students found\n")
    else:
        for row in rows:
            print(f"{row[0]}. Name: {row[1]}, Age: {row[2]}")
    print()


def menu():
    while True:
        print("======= STUDENT MANAGEMENT SYSTEM =======")
        print("1. Add student")
        print("2. View students")
        print("3. Exit")

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
conn.close()
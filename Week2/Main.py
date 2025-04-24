from Student import Student
from Utils import calculate_class_average, find_top_student, find_bottom_student, display_all_students

students = []

def add_student():
    name = input("Enter student name: ")
    grades_str = input("Enter grades separated by spaces: ")
    grades = list(map(int, grades_str.split()))
    students.append(Student(name, grades))

def remove_student():
    name = input("Enter the name of the student to remove: ")
    global students
    students = [s for s in students if s.name != name]

def menu():
    while True:
        print("\n-- Student Grades Tracker --")
        print("1. Add Student")
        print("2. Remove Student")
        print("3. View All Students")
        print("4. Class Average")
        print("5. Top Performer")
        print("6. Bottom Performer")
        print("7. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            add_student()
        elif choice == "2":
            remove_student()
        elif choice == "3":
            display_all_students(students)
        elif choice == "4":
            print(f"Class Average: {calculate_class_average(students):.2f}")
        elif choice == "5":
            top = find_top_student(students)
            print(f"Top Student: {top}" if top else "No students yet.")
        elif choice == "6":
            bottom = find_bottom_student(students)
            print(f"Bottom Student: {bottom}" if bottom else "No students yet.")
        elif choice == "7":
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    menu()

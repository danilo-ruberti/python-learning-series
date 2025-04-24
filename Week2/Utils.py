### utils.py ###

def calculate_class_average(students):
    if not students:
        return 0
    return sum(student.average() for student in students) / len(students)

def find_top_student(students):
    return max(students, key=lambda s: s.average(), default=None)

def find_bottom_student(students):
    return min(students, key=lambda s: s.average(), default=None)


def display_all_students(students):
    for student in students:
        print(student)
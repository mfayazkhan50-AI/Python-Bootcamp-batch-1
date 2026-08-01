numbers = [2, 1, 5, 3, 0, 4]

sorted_list = sorted(numbers)

print(sorted_list)

students = [
    ('ali', 100),
    ('ahmed', 20),
    ('sara', 60)
]

def sort_student(student):
    return student[1]


# sorted(iterble, key=function, reverse=boolean)
sorted_students = sorted(students, key=sort_student, reverse=True)

print(sorted_students)
# dict methods

# 1. get()

students = {'name':'yasir',
            'roll_no':'225',
            'class': '12th',
            'marks': '512'}

print(students.get('age'))

# 2. keys
print(students.keys())

# 3. values
print(students.values())

# 4. items
print(students.items())

# 5. pop
print(students.pop('name'))

# 6. update
students.update({'name': 'Aslam'})
print(students)
students = {'name':'yasir',
            'roll_no':'225',
            'class': '12th',
            'marks': '512'}

print('before update', students)

# update
students['name'] = 'Imran'

print('after update', students)

# add
students['age'] = 20
print('after adding', students)

# removing
del students['age']
print(students)



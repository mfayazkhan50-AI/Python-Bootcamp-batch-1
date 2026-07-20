
# dictionary stores uniques keys

# nested dictionaries
class_12th = {'s1': {'key1': 'value1','key1': 'value1'},
              's2': {'key1': 'value1','key1': 'value1'}}




class_data = {'s1': {'name':'yasir',
            'roll_no':'225',
            'class': '12th',
            'marks': '512'},

            's2': {'name': 'aslam',
            'roll_no':'230',
            'class': '12th',
            'marks': '452'}}

print(class_data['s2']['name'])

# looping
students = {'name':'yasir',
            'roll_no':'225',
            'class': '12th',
            'marks': '512'}

for key, value in students.items():


    print(key,':', value)


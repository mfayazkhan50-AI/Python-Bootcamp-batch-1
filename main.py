print('==== Students Record System ====')

students = {}

# {'name1':{'subj1': value, 'sub2': value, 'sub3': value},
#   'name2': {'subj1': value, 'sub2': value, 'sub3': value}}

while True:
    

    print('''
    Choose one option:
    1. Add Student
    2. Update Student
    3. View Students
    4. Search Student
    5. Delete Student
    6. Exit
    ''')

    user_choice = input('Choose one option(1, 6): ').strip()

    if user_choice == '1':
        print('Adding students')
        name = input('Enter the student name: ').capitalize()  #imran -> Imran
        maths = int(input('Enter the marks of maths: '))
        english = int(input('Enter the marks of english: '))
        urdu = int(input('Enter the marks of urdu: '))

        students[name] = {'maths': maths,
                        'english': english,
                        'urdu': urdu}
        print('--->>>>  Record Added Successfully')


    elif user_choice == '2':
        print('Updating Students')
        name = input('Enter the student name: ').capitalize()

        if name in students:
            print('student found')
            updated_maths = int(input('Enter the marks of maths: '))
            updated_english = int(input('Enter the marks of english: '))
            updated_urdu = int(input('Enter the marks of urdu: '))

            students[name]['maths'] = updated_maths
            students[name]['english'] = updated_english
            students[name]['urdu'] = updated_urdu

            print('---->>>>  Record Updated Successfully')

        else:
            print('Error: Student not found')


    elif user_choice == '3':
        print('View Students\n')

        for name in students:
            print(name)
            print(f'Maths score: {students[name]['maths']}')
            print(f'English score: {students[name]['english']}')
            print(f'Urdu score: {students[name]['urdu']}')
            print('-'*20)
            print('\n')



    elif user_choice == '4':
        print('Search Students')
        name = input('Enter the student name: ').capitalize()

        if name in students:
            print(f'\nRecord of {name}\n')
            print(f'Maths score: {students[name]['maths']}')
            print(f'English score: {students[name]['english']}')
            print(f'Urdu score: {students[name]['urdu']}')

        else:
            print('Error: Student not found')
        

    elif user_choice == '5':
        print('Deleting Record')

        name = input('Enter the name of Student: ').capitalize()
        if name in students:

            del students[name]
            print(f'--->>> Record Deleted {name}')

        else:
            print('Error: Student no found')


    elif user_choice == '6':
        print('\n-- Thank you So Much have a good day --')
        break










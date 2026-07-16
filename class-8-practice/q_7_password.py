while True:

    password = 'python123'

    user_password = input('Enter the password: ')

    if (user_password == password):
        print('Access Granted')
        break

    else:
        print('Wrong password')
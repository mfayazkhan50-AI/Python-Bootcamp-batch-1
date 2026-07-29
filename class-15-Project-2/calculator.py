op = None
num1 = 0
num2 = 0



def addition():
    result = num1 + num2
    print('Addition: ',result)

def subtraction():
    result = num1 - num2
    print('Subtraction: ',result)

def multiplication():
    result = num1 * num2
    print('Multiplication: ',result)

def division():
    result = num1 / num2
    print('Division: ',result)




while True:
   
    try:
        num1 = int(input('Enter 1st value: '))
        op = input('Enter the operator(+, -, /, *): ')
        num2 = int(input('Enter second value: '))

    except ValueError as e:
        print(e)


    if op == '+':
        addition()

    elif op == '-':
        subtraction()

    elif op == '*':
        multiplication()

    elif op == '/':
        try:
            division()
        except ZeroDivisionError:
            print('Zero Division Error---')

    else:
        print('Invalid Input...')


    print('-'*50)
    user_input = input('Enter q to Exit Or \npress any and Enter to continue: ').lower()

    if user_input == 'q':
        print('\n----- Ok Have a Good Day -------')
        break 

    print('-'*50)

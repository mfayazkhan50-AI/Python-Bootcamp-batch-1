num1 = int(input('Enter num1: '))

operator = input('Enter the operator: (+, -, /, *): ')

num2 = int(input('Enter num2: '))

if operator == '+':
    print(f'Addition = {num1+num2}')

elif operator == '-':
    print(f'Subtraction = {num1 - num2}')

elif operator == '*':
    print(f'product = {num1 * num2}')

elif operator == '/':
    print(f'Division = {num1 - num2}')

else:
    print('Invalid operator')










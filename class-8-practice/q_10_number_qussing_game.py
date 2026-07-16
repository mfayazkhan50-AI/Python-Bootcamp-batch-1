secret = 36

while True:
    user_input = int(input('guess the number: '))

    if (user_input < secret):
        print('Too low')

    elif (user_input > secret):
        print('too high')

    elif (user_input == secret):
        print('Congratulations you got the number')
        break

print('Game is over')

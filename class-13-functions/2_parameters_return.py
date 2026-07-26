def account(username, amount, due_data):

    print(f'hello {username}, your bill is ${amount} due to {due_data}')


account('Tahir', 450, '1/8/2026')
account('Rehan', 650, '2/8/2026')


print('-'*50)

def sum(a, b):
    return a+b


a = sum(5, 6)
print('value of a: ', a)

def user_max(a, b):
    if a>b:
        return a
    else:
        return b


print(user_max(0, 2))



def print_karo(a):
    print(a)



print_karo('hello world')



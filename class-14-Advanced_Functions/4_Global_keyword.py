# global keyword
a = 278

def change_value():
    # local variable
    global a
    a = 378

    print('inside running a: ', a)



print('before calling: ', a)
change_value()

print('outside running:', a)
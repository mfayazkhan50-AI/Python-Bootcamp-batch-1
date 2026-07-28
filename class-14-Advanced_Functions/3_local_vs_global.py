# Local vs Global variables

def hello():
    # local variable
    a = 90
    print('inside fucnton value of a:', a)

hello()


# print('outside the fucnton value of a:', a)


print('----------- GLOBAL VARIABLE----------')

#  global varable
a = 234

def hello():
    # local variable
    a = 78
    print('after changing a: ', a)




hello()

print('after changing the value inside function:', a)



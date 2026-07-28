# positional args take any number of data
# values of *args are returned in a tuple

def greet(*name):

    print(name)


greet('aslam', 'ali', 4, 'hook')

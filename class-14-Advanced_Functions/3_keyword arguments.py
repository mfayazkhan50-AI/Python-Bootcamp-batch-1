# keyword args
# keyword args take any number of data
# collect the values and returned in a dictionary
# syntax -> **kewargs

def students(**data):
    print(data)


students(name='ali', marks=650)


print('-'*30)


def demo(a, *args, **kwargs):
    print(a, args, kwargs)

demo(1, 2, 3, 4, 5, x=5, y=6)

# 1 (2, 3) {'x': 5}


def square(x):
    return x * x

numbers = [1, 3, 4]

# map(function, iterable)

s_numbers = list(map(square, numbers))
print(s_numbers)


s_numbers2 = list(map(lambda x: x * x, numbers))

print(s_numbers2)
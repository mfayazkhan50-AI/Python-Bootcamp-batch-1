a = {1, 2, 3, 4}
b = {3, 4, 5, 6}

print(a.symmetric_difference(b))   # {1, 2, 5, 6}

e = {1, 2}
print(a.issubset(e))

d = e.issuperset(a)
print(d) # True
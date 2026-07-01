'''
and
value1 | value2 | output
1      | 1      | True
1      | 0      | False
0      | 1      | False
0      | 0      | False

or
value1 | value2 | output
1      | 1      | True
1      | 0      | True
0      | 1      | True
0      | 0      | False

NOT
value | output
1     | 0
0     | 1
'''

age = 28

# and
print('and')
print(age >= 18 and age < 30)


# or
print('OR')
print(age == 18 or age == 30)

# not
print('not')
print(not(age == 18 or age == 30))
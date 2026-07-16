n = int(input('Enter the number: '))
456

count = 0
while (n>0):
    
    n = n // 10
    count = count + 1
    
print('Digits: ', count)
print(len(n))
    
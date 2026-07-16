num = int(input('Enter the number: '))

temp = num
reversed_num = 0

while (temp>0):

    digit = temp % 10

    reversed_num = reversed_num * 10 + digit 
    
    temp = temp // 10

print(reversed_num)




    
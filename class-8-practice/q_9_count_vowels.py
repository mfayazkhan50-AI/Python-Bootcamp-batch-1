word = input('Enter a word: ') # pakistan

i = 0
count = 0

for i in word:
    
    if i in 'aeiou':
        count = count + 1
    
print(count)
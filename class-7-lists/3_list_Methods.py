items = ['apple', 'orange', 'potato', 'onion', 'banana', 'apple', 'apple']

# 1. append() - add one item at the end
items.append('berry')
print("After append:", items)

# 2. insert() - add item at a specific position
items.insert(2, 'grapes')
print("After insert:", items)

# 3. len() - get the length of the list
print("Length:", len(items))

# 4. count() - count how many times a value appears
print("Count of 'apple':", items.count('apple'))

# 5. index() - find the index of a value
print("Index of 'onion':", items.index('onion'))

# 6. remove() - remove an item by value (removes the FIRST match)
items.remove('apple')
print("After remove:", items)

# 7. sort() - arrange the list in order (alphabetical for strings)
items.sort()
print("After sort:", items)

# 8. reverse() - flip the list backward
items.reverse()
print("After reverse:", items)

# 9. pop() - remove and return the last item
removed_item = items.pop()
print("Popped item:", removed_item)
print("After pop:", items)

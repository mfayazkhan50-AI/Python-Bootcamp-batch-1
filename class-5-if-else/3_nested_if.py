age = int(input('Enter your age: '))

has_id = (input('has id: (True, False): '))

if age >= 18:

    if has_id == 'True':
        print("Entry allowed")
    else:
        print("ID required")

        
else:
    print("Too young")
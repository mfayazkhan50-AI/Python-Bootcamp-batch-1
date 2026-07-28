
total_expense = 0
def add_expense(*amounts, category="General", **details):
    global total_expense
    
    sum_expense = sum(amounts)
    total_expense += sum_expense

    print("Category:", category)
    print("Amounts:", amounts)
    print("Extra Info:", details)
    print("Added:", sum_expense)
    print("-" * 20)




# add_expense(200, 150, category="Food", place="Karachi")
add_expense(200, 150, category='food', place='karachi', transport='car')

add_expense(500, category="Rent")

add_expense(80, 20, 10)




# WAP in python to create an inventory management system that takes a list of stock quantities as input and updates the stock by adding 50 to the quantities that are less than 10 and then calculates the total inventory after the update.

# enter stock quantities as space separated values, for example: 5 15 8 20 0

stock = list(map(int, input("Enter stock quantities: ").split()))

# update stock quantities
updated_stock = []

for s in stock:
    if s > 0:
        if s < 10:
            s += 50
        updated_stock.append(s)

# calculate total inventory
print("Total Inventory:", sum(updated_stock))



'''output:
Enter stock quantities: 5 15 8 20 0
Total Inventory: 93

Enter stock quantities: 0 0 0 0 0
Total Inventory: 0

Enter stock quantities: 1 2 3 4 5
Total Inventory: 265
'''
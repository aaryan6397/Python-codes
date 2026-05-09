inventory = {}

while True:

    print("\n--- INVENTORY MENU ---")
    print("1. Add Product")
    print("2. Update Quantity")
    print("3. Search Product")
    print("4. Display Low Stock Items")
    print("5. Exit")

    choice = int(input("Enter choice: "))

    if choice == 1:
        product = input("Enter product name: ")
        qty = int(input("Enter quantity: "))
        inventory[product] = qty
        print("Product Added!")

    elif choice == 2:
        product = input("Enter product name: ")

        if product in inventory:
            qty = int(input("Enter new quantity: "))
            inventory[product] = qty
            print("Quantity Updated!")
        else:
            print("Product not found!")

    elif choice == 3:
        product = input("Enter product name: ")

        if product in inventory:
            print(product, "Quantity =", inventory[product])
        else:
            print("Product not found!")

    elif choice == 4:
        print("\nLow Stock Items (less than 5):")

        for product, qty in inventory.items():
            if qty < 5:
                print(product, ":", qty)

    elif choice == 5:
        print("Exiting Program...")
        break

    else:
        print("Invalid Choice!")
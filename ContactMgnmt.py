contacts = {}

while True:

    print("\n--- CONTACT MANAGEMENT SYSTEM ---")
    print("1. Add Contact")
    print("2. Update Contact")
    print("3. Search Contact")
    print("4. Delete Contact")
    print("5. Display All Contacts")
    print("6. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:

        name = input("Enter name: ")
        number = input("Enter phone number: ")

        contacts[name] = number

        print("Contact Added!")

    elif choice == 2:

        name = input("Enter contact name to update: ")

        if name in contacts:

            new_number = input("Enter new number: ")

            contacts[name] = new_number

            print("Contact Updated!")

        else:
            print("Contact not found!")

    elif choice == 3:

        name = input("Enter contact name to search: ")

        if name in contacts:
            print(name, ":", contacts[name])

        else:
            print("Contact not found!")

    elif choice == 4:

        name = input("Enter contact name to delete: ")

        if name in contacts:

            del contacts[name]

            print("Contact Deleted!")

        else:
            print("Contact not found!")

    elif choice == 5:

        print("\nAll Contacts:")

        for name, number in contacts.items():
            print(name, ":", number)

    elif choice == 6:

        print("Exiting Program...")
        break

    else:
        print("Invalid Choice!")
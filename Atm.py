correct_pin = "1234"
attempts = 0
max_attempts = 3

while attempts < max_attempts:

    pin = input("Enter ATM PIN: ")

    if pin == correct_pin:

        print("Access Granted!")
        break

    else:

        attempts += 1

        print("Invalid PIN")

        remaining = max_attempts - attempts

        if remaining > 0:
            print("Attempts remaining:", remaining)

if attempts == max_attempts:
    print("Account Locked due to 3 invalid attempts.")
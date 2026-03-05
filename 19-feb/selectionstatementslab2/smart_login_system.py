'''2. Smart Login System Create a login system with: 
• Username validation 
• Password validation 
• Maximum 3 failed attempts 
If 3 attempts fail, lock the account.'''


# predefined credentials
correct_username = "admin"
correct_password = "1234"

attempts = 0
max_attempts = 3

# login loop
while attempts < max_attempts:

    username = input("Enter username: ")
    password = input("Enter password: ")

    # validation check
    if username == correct_username and password == correct_password:
        print("Login successful!")
        break
    else:
        attempts += 1
        print("Invalid credentials. Attempt:", attempts)

# account lock condition
if attempts == max_attempts:
    print("Account locked due to 3 failed attempts.")


    '''output:
Enter username: admin
Enter password: 1234
Login successful!

Enter username: user
Enter password: pass
Invalid credentials. Attempt: 1

Enter username: admin
Enter password: wrong
Invalid credentials. Attempt: 2

Enter username: admin
Enter password: wrong
Invalid credentials. Attempt: 3

Account locked due to 3 failed attempts.
'''
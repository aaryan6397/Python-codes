# Problem Statement: Validate username and password.
# Input Format: Read input from standard input.
# Output Format: Print the required output.
# Constraints: Standard constraints apply.

# Read username and password from user input..
username = input("Enter your username : ")
password = input("Enter your password : ")

if(username == "admin" and password == "admin123"):
    print("Login successful")
else: 
    print("Invalid username  or password")

# output
# Enter your username : admin
# Enter your password : admin123
# Login successful
# Program: Check voting eligibility
# age >= 18 then eligible

# input
age = int(input("Enter your age: "))

# condition
if age >= 18:
    print("You are eligible to vote")
else:
    print("You are not eligible to vote")

'''output:
Enter your age: 20
You are eligible to vote

Enter your age: 15
You are not eligible to vote

Enter your age: 18
You are eligible to vote
'''
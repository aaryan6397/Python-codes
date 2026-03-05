# this program will validate the age of a person. It will check if the age is greater than 0 and print "Valid age" if it is, otherwise it will print "Invalid age".
#  The program will also demonstrate the correct and incorrect way to use if statements in Python.


# Enter the age of the person
age=int(input("Enter you age: "))

# This is the wrong way to use if statement
if(age>0):
    print("Valid age")
if(age<=0):
    print("Invalid age")

print("Note: this is the wrong way to use if statement")

# This is the right way to use if statement

print("Note: this is the right way to use if statement")

if(age>0):
    print("Valid age")
else:
    print("Invalid age")

'''output:
Enter you age: 25
Note: this is the wrong way to use if statement
Valid age
Note: this is the right way to use if statement
Valid age
'''
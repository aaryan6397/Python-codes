# Program: Check number range

# input
num = int(input("Enter a number: "))

# condition
if num < 0:
    print("Number is Negative")
elif num >= 0 and num <= 50:
    print("Number is between 0 and 50")
elif num > 50 and num <= 100:
    print("Number is between 51 and 100")
else:
    print("Number is greater than 100")

'''output:

Enter a number: -5
Number is Negative 
 
Enter a number: 25
Number is between 0 and 50

Enter a number: 75
Number is between 51 and 100

Enter a number: 150
Number is greater than 100
'''

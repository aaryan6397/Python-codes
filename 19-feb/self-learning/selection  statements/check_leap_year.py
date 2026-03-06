# Program: Check whether a year is leap year

# input
year = int(input("Enter a year: "))

# leap year condition
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print("Leap Year")
else:
    print("Not a Leap Year")

'''output:
Enter a year: 2020
Leap Year

Enter a year: 2021
Not a Leap Year

Enter a year: 1900
Not a Leap Year

Enter a year: 2000
Leap Year

Enter a year: 2024
Leap Year
'''

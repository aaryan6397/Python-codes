# Problem 20
# Problem Statement: Find the greatest of four numbers.
# Input Format: Read input from standard input.
# Output Format: Print the required output.
# Constraints: Standard constraints apply.




# Read four numbers from user input
num1 = float(input("Enter the first Number : "))
num2 = float(input("Enter the second Number : "))
num3 = float(input("Enter the third Number : "))
num4 = float(input("Enter the fourth Number : "))

if(num1 >=num2 and num1 >= num3 and num1 >= num4):
    print("The greatest number is : ", num1)
elif(num2 >= num1 and num2 >= num3 and num2 >= num4):
        print("The greatest number is : ", num2)
elif(num3 >= num1 and num3 >= num2 and num3 >= num4):
        print("The greatest number is : ", num3)
elif(num4 >= num1 and num4 >= num2 and num4 >= num3):
        print("The greatest number is : ", num4)
else:
        print("All numbers are equal")       

# output
# Enter the first Number : 12
# Enter the second Number : 21
# Enter the third Number : 32
# Enter the fourth Number : 2
# The greatest number is :  32.0

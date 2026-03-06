# Program: Find factorial of a number

# input
num = int(input("Enter a number: "))

# factorial variable
factorial = 1

# loop
for i in range(1, num + 1):
    factorial *= i

# output
print("Factorial =", factorial)



'''output:

Enter a number: 5
Factorial = 120 


Explanation:
The program calculates the factorial of a number using a for loop. It initializes a variable factorial to
1 and iterates from 1 to num, multiplying each number with factorial. Finally, it prints the result.
'''
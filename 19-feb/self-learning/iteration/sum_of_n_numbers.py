# Program: Calculate sum of first n numbers

# user se input lena
n = int(input("Enter a number: "))

# sum variable initialize
total = 0

# loop chalana
for i in range(1, n + 1):
    total += i   # total = total + i

# result print
print("Sum =", total)




'''output:
  
Enter a number: 5
Sum = 15


Explanation:
The program calculates the sum of the first n numbers using a for loop. It initializes a variable
total to 0 and iterates from 1 to n, adding each number to total. Finally, it prints the result.
'''
# Program: Check whether a number is prime

# input
num = int(input("Enter a number: "))

is_prime = True

# loop from 2 to num-1
for i in range(2, num):
    if num % i == 0:
        is_prime = False
        break

# result
if is_prime:
    print("Prime Number")
else:
    print("Not a Prime Number")


'''output:
Enter a number: 7
Prime Number

Enter a number: 10
Not a Prime Number 
 
Explanation:
The program checks if a number is prime by iterating from 2 to num-1 and
checking if num is divisible by any of those numbers. If it is divisible, it sets is_prime to False and breaks the loop. Finally, it prints whether the number is prime or not.
'''
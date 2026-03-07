# main_prime.py

import multiple_logic as prime_module

# Input from user
num = int(input("Enter number: "))

# Check prime or not
if prime_module.is_prime(num):
    print("Prime Number")
else:
    print("Not Prime Number")



'''output:
Enter number: 17
Prime Number
'''
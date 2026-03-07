# evenodd_module.py
# Function to check even or odd number

def check_even_odd(n):
    # Check if number is divisible by 2
    if n % 2 == 0:
        return "Even Number"
    else:
        return "Odd Number"
    



    # factorial_module.py
# Function to calculate factorial

def factorial(n):
    fact = 1
    # Loop to multiply numbers
    for i in range(1, n+1):
        fact = fact * i
    return fact




# largest_module.py
# Function to find largest of three numbers

def largest(a, b, c):
    # Using built-in max() function
    return max(a, b, c)




# prime_module.py
# Function to check prime number

def is_prime(n):
    # Numbers less than 2 are not prime
    if n <= 1:
        return False
    
    # Loop to check divisibility
    for i in range(2, n):
        if n % i == 0:
            return False
    
    return True






# circle_module.py
# Function to calculate area of circle

def area(radius):
    # Formula: πr²
    return 3.14 * radius * radius




# reverse_module.py
# Function to reverse a string

def reverse(text):
    # Slicing method to reverse string
    return text[::-1]





# fibonacci_module.py
# Function to print Fibonacci series

def fibonacci(n):
    a = 0
    b = 1

    # Loop to print series
    for i in range(n):
        print(a, end=" ")
        a, b = b, a + b




        # vowel_module.py
# Function to count vowels in a string

def count_vowels(text):
    vowels = "aeiouAEIOU"
    count = 0

    # Loop through characters
    for ch in text:
        if ch in vowels:
            count += 1

    return count
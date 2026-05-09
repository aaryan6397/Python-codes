# Program to generate first N prime numbers

n = int(input("Enter the value of N: "))

count = 0
num = 2
prime_list = []
sum_prime = 0

while count < n:
    is_prime = True

    for i in range(2, num):
        if num % i == 0:
            is_prime = False
            break

    if is_prime:
        prime_list.append(num)
        sum_prime += num
        count += 1

    num += 1

# Calculate average
average = sum_prime / n

# Display results
print("\nFirst", n, "Prime Numbers:")
print(prime_list)

print("Sum of Prime Numbers =", sum_prime)
print("Average of Prime Numbers =", average)
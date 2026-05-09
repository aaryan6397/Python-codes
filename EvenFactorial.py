def factorial(n):
    fact = 1

    for i in range(1, n + 1):
        fact *= i

    return fact


def even_factorials(numbers):

    result = []

    for num in numbers:
        if num % 2 == 0:
            result.append(factorial(num))

    return result


nums = [2, 3, 4, 5, 6]

print("Factorials of Even Numbers:")
print(even_factorials(nums))
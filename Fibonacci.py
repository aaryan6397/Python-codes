def fibonacci_even(n):

    a, b = 0, 1
    even_list = []

    print("Fibonacci Series:")

    while a <= n:
        print(a, end=" ")

        if a % 2 == 0:
            even_list.append(a)

        a, b = b, a + b

    print("\n\nEven Fibonacci Numbers:")
    print(even_list)


num = int(input("Enter limit: "))
fibonacci_even(num)
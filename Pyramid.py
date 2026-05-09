rows = int(input("Enter number of rows: "))

total_sum = 0

for i in range(1, rows + 1):

    for j in range(1, i + 1):
        print(j, end=" ")
        total_sum += j

    print()

print("\nSum of all numbers =", total_sum)
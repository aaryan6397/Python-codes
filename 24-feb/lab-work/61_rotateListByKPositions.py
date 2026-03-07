# Problem 61
# Problem Statement: Rotate a list by K positions.
# Input Format: Read input from standard input.
# Output Format: Print the required output.
# Constraints: Standard constraints apply.

n = int(input("Enter number of elements : "))
my_list = []
for i in range(n):
    element = int(input("Enter element : "))
    my_list.append(element)

k = int(input("Enter number of positions to rotate : "))

print("Original list :", my_list)

k = k % len(my_list)
rotated_list = my_list[k:] + my_list[:k]

print("Rotated list :", rotated_list)

# output
# Enter number of elements : 5
# Enter element : 10
# Enter element : 20
# Enter element : 30
# Enter element : 40
# Enter element : 50
# Enter number of positions to rotate : 2
# Original list : [10, 20, 30, 40, 50]
# Rotated list : [30, 40, 50, 10, 20]
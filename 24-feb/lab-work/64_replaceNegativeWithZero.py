# Problem 64
# Problem Statement: Replace negative numbers with zero.
# Input Format: Read input from standard input.
# Output Format: Print the required output.
# Constraints: Standard constraints apply.

n = int(input("Enter number of elements : "))
my_list = []
for i in range(n):
    element = int(input("Enter element : "))
    my_list.append(element)

print("Original list :", my_list)

for i in range(len(my_list)):
    if my_list[i] < 0:
        my_list[i] = 0

print("List after replacing negatives with zero :", my_list)

# output
# Enter number of elements : 6
# Enter element : 5
# Enter element : -3
# Enter element : 8
# Enter element : -1
# Enter element : 10
# Enter element : -7
# Original list : [5, -3, 8, -1, 10, -7]
# List after replacing negatives with zero : [5, 0, 8, 0, 10, 0]
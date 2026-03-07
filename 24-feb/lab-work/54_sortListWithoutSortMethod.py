# Problem 54
# Problem Statement: Sort a list without using sort method.
# Input Format: Read input from standard input.
# Output Format: Print the required output.
# Constraints: Standard constraints apply.

n = int(input("Enter number of elements : "))
my_list = []
for i in range(n):
    element = int(input("Enter element : "))
    my_list.append(element)

print("Original list :", my_list)

# Bubble sort
for i in range(len(my_list)):
    for j in range(len(my_list) - i - 1):
        if my_list[j] > my_list[j + 1]:
            my_list[j], my_list[j + 1] = my_list[j + 1], my_list[j]

print("Sorted list :", my_list)

# output
# Enter number of elements : 5
# Enter element : 34
# Enter element : 12
# Enter element : 45
# Enter element : 9
# Enter element : 23
# Original list : [34, 12, 45, 9, 23]
# Sorted list : [9, 12, 23, 34, 45]
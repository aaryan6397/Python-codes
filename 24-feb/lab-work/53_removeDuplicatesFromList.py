# Problem 53
# Problem Statement: Remove duplicate elements from list.
# Input Format: Read input from standard input.
# Output Format: Print the required output.
# Constraints: Standard constraints apply.

n = int(input("Enter number of elements : "))
my_list = []
for i in range(n):
    element = int(input("Enter element : "))
    my_list.append(element)

unique_list = []
for item in my_list:
    if item not in unique_list:
        unique_list.append(item)

print("Original list :", my_list)
print("List after removing duplicates :", unique_list)

# output
# Enter number of elements : 7
# Enter element : 1
# Enter element : 2
# Enter element : 3
# Enter element : 2
# Enter element : 1
# Enter element : 4
# Enter element : 3
# Original list : [1, 2, 3, 2, 1, 4, 3]
# List after removing duplicates : [1, 2, 3, 4]
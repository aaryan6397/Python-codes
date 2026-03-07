# Problem 60
# Problem Statement: Find common elements between two lists.
# Input Format: Read input from standard input.
# Output Format: Print the required output.
# Constraints: Standard constraints apply.

n1 = int(input("Enter number of elements in list 1 : "))
list1 = []
for i in range(n1):
    element = int(input("Enter element : "))
    list1.append(element)

n2 = int(input("Enter number of elements in list 2 : "))
list2 = []
for i in range(n2):
    element = int(input("Enter element : "))
    list2.append(element)

common = []
for item in list1:
    if item in list2 and item not in common:
        common.append(item)

print("List 1 :", list1)
print("List 2 :", list2)
print("Common elements :", common)

# output
# Enter number of elements in list 1 : 5
# Enter element : 1
# Enter element : 2
# Enter element : 3
# Enter element : 4
# Enter element : 5
# Enter number of elements in list 2 : 5
# Enter element : 3
# Enter element : 4
# Enter element : 5
# Enter element : 6
# Enter element : 7
# List 1 : [1, 2, 3, 4, 5]
# List 2 : [3, 4, 5, 6, 7]
# Common elements : [3, 4, 5]
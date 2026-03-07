# Problem 58
# Problem Statement: Merge two lists and remove duplicates.
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

merged_list = list1 + list2

unique_list = []
for item in merged_list:
    if item not in unique_list:
        unique_list.append(item)

print("List 1 :", list1)
print("List 2 :", list2)
print("Merged list without duplicates :", unique_list)

# output
# Enter number of elements in list 1 : 4
# Enter element : 1
# Enter element : 2
# Enter element : 3
# Enter element : 4
# Enter number of elements in list 2 : 4
# Enter element : 3
# Enter element : 4
# Enter element : 5
# Enter element : 6
# List 1 : [1, 2, 3, 4]
# List 2 : [3, 4, 5, 6]
# Merged list without duplicates : [1, 2, 3, 4, 5, 6]
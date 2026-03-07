# Problem 49
# Problem Statement: Return unique elements from a list using function.
# Input Format: Read input from standard input.
# Output Format: Print the required output.
# Constraints: Standard constraints apply.

def unique_elements(lst):
    unique = []
    for item in lst:
        if item not in unique:
            unique.append(item)
    return unique

n = int(input("Enter number of elements : "))
my_list = []
for i in range(n):
    element = int(input("Enter element : "))
    my_list.append(element)

result = unique_elements(my_list)
print("Unique elements are :", result)

# output
# Enter number of elements : 6
# Enter element : 1
# Enter element : 2
# Enter element : 3
# Enter element : 2
# Enter element : 1
# Enter element : 4
# Unique elements are : [1, 2, 3, 4]
# Problem 68
# Problem Statement: Convert tuple to list.
# Input Format: Read input from standard input.
# Output Format: Print the required output.
# Constraints: Standard constraints apply.

n = int(input("Enter number of elements : "))
my_list = []
for i in range(n):
    element = int(input("Enter element : "))
    my_list.append(element)

my_tuple = tuple(my_list)

converted_list = []
for item in my_tuple:
    converted_list.append(item)

print("Tuple :", my_tuple)
print("Converted list :", converted_list)

# output
# Enter number of elements : 4
# Enter element : 10
# Enter element : 20
# Enter element : 30
# Enter element : 40
# Tuple : (10, 20, 30, 40)
# Converted list : [10, 20, 30, 40]

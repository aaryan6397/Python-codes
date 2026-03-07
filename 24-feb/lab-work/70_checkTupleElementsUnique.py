# Problem 70
# Problem Statement: Check whether tuple elements are unique.
# Input Format: Read input from standard input.
# Output Format: Print the required output.
# Constraints: Standard constraints apply.

n = int(input("Enter number of elements : "))
my_list = []
for i in range(n):
    element = int(input("Enter element : "))
    my_list.append(element)

my_tuple = tuple(my_list)

is_unique = True
for i in range(len(my_tuple)):
    for j in range(i + 1, len(my_tuple)):
        if my_tuple[i] == my_tuple[j]:
            is_unique = False
            break

print("Tuple :", my_tuple)

if is_unique:
    print("All elements in the tuple are unique")
else:
    print("Tuple has duplicate elements")

# output
# Enter number of elements : 5
# Enter element : 10
# Enter element : 20
# Enter element : 30
# Enter element : 40
# Enter element : 50
# Tuple : (10, 20, 30, 40, 50)
# All elements in the tuple are unique
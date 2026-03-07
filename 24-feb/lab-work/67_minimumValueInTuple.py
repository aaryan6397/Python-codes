# Problem 67
# Problem Statement: Find minimum value in a tuple.
# Input Format: Read input from standard input.
# Output Format: Print the required output.
# Constraints: Standard constraints apply.

n = int(input("Enter number of elements : "))
my_list = []
for i in range(n):
    element = int(input("Enter element : "))
    my_list.append(element)

my_tuple = tuple(my_list)

minimum = my_tuple[0]
for num in my_tuple:
    if num < minimum:
        minimum = num

print("Tuple :", my_tuple)
print("Minimum value in the tuple is :", minimum)

# output
# Enter number of elements : 5
# Enter element : 10
# Enter element : 25
# Enter element : 3
# Enter element : 42
# Enter element : 15
# Tuple : (10, 25, 3, 42, 15)
# Minimum value in the tuple is : 3
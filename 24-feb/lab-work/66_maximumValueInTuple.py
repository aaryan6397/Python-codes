# Problem 66
# Problem Statement: Find maximum value in a tuple.
# Input Format: Read input from standard input.
# Output Format: Print the required output.
# Constraints: Standard constraints apply.

n = int(input("Enter number of elements : "))
my_list = []
for i in range(n):
    element = int(input("Enter element : "))
    my_list.append(element)

my_tuple = tuple(my_list)

maximum = my_tuple[0]
for num in my_tuple:
    if num > maximum:
        maximum = num

print("Tuple :", my_tuple)
print("Maximum value in the tuple is :", maximum)

# output
# Enter number of elements : 5
# Enter element : 10
# Enter element : 25
# Enter element : 8
# Enter element : 42
# Enter element : 15
# Tuple : (10, 25, 8, 42, 15)
# Maximum value in the tuple is : 42
# Problem 69
# Problem Statement: Count occurrence of element in tuple.
# Input Format: Read input from standard input.
# Output Format: Print the required output.
# Constraints: Standard constraints apply.

n = int(input("Enter number of elements : "))
my_list = []
for i in range(n):
    element = int(input("Enter element : "))
    my_list.append(element)

my_tuple = tuple(my_list)

search = int(input("Enter element to count : "))

count = 0
for item in my_tuple:
    if item == search:
        count += 1

print("Tuple :", my_tuple)
print("Occurrence of", search, "in tuple is :", count)

# output
# Enter number of elements : 7
# Enter element : 1
# Enter element : 2
# Enter element : 3
# Enter element : 2
# Enter element : 1
# Enter element : 2
# Enter element : 4
# Enter element to count : 2
# Tuple : (1, 2, 3, 2, 1, 2, 4)
# Occurrence of 2 in tuple is : 3
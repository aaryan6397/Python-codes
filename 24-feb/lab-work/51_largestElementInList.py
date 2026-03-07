# Problem 51
# Problem Statement: Find largest element in a list.
# Input Format: Read input from standard input.
# Output Format: Print the required output.
# Constraints: Standard constraints apply.

n = int(input("Enter number of elements : "))
my_list = []
for i in range(n):
    element = int(input("Enter element : "))
    my_list.append(element)

largest = my_list[0]
for num in my_list:
    if num > largest:
        largest = num

print("Largest element in the list is :", largest)

# output
# Enter number of elements : 5
# Enter element : 10
# Enter element : 25
# Enter element : 8
# Enter element : 42
# Enter element : 15
# Largest element in the list is : 42
# Problem 52
# Problem Statement: Find smallest element in a list.
# Input Format: Read input from standard input.
# Output Format: Print the required output.
# Constraints: Standard constraints apply.

n = int(input("Enter number of elements : "))
my_list = []
for i in range(n):
    element = int(input("Enter element : "))
    my_list.append(element)

smallest = my_list[0]
for num in my_list:
    if num < smallest:
        smallest = num

print("Smallest element in the list is :", smallest)

# output
# Enter number of elements : 5
# Enter element : 10
# Enter element : 25
# Enter element : 3
# Enter element : 42
# Enter element : 15
# Smallest element in the list is : 3
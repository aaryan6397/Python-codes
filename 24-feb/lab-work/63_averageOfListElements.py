# Problem 63
# Problem Statement: Find average of list elements.
# Input Format: Read input from standard input.
# Output Format: Print the required output.
# Constraints: Standard constraints apply.

n = int(input("Enter number of elements : "))
my_list = []
for i in range(n):
    element = int(input("Enter element : "))
    my_list.append(element)

total = 0
for num in my_list:
    total = total + num

average = total / len(my_list)

print("List :", my_list)
print("Average of list elements is :", average)

# output
# Enter number of elements : 5
# Enter element : 10
# Enter element : 20
# Enter element : 30
# Enter element : 40
# Enter element : 50
# List : [10, 20, 30, 40, 50]
# Average of list elements is : 30.0
# Problem 65
# Problem Statement: Check whether list is palindrome.
# Input Format: Read input from standard input.
# Output Format: Print the required output.
# Constraints: Standard constraints apply.

n = int(input("Enter number of elements : "))
my_list = []
for i in range(n):
    element = int(input("Enter element : "))
    my_list.append(element)

reversed_list = my_list[::-1]

print("List :", my_list)

if my_list == reversed_list:
    print("List is a Palindrome")
else:
    print("List is not a Palindrome")

# output
# Enter number of elements : 5
# Enter element : 1
# Enter element : 2
# Enter element : 3
# Enter element : 2
# Enter element : 1
# List : [1, 2, 3, 2, 1]
# List is a Palindrome
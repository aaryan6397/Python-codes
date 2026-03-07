# Problem 59
# Problem Statement: Separate even and odd numbers from list.
# Input Format: Read input from standard input.
# Output Format: Print the required output.
# Constraints: Standard constraints apply.

n = int(input("Enter number of elements : "))
my_list = []
for i in range(n):
    element = int(input("Enter element : "))
    my_list.append(element)

even_list = []
odd_list = []

for num in my_list:
    if num % 2 == 0:
        even_list.append(num)
    else:
        odd_list.append(num)

print("Original list :", my_list)
print("Even numbers :", even_list)
print("Odd numbers :", odd_list)

# output
# Enter number of elements : 6
# Enter element : 10
# Enter element : 15
# Enter element : 22
# Enter element : 33
# Enter element : 40
# Enter element : 7
# Original list : [10, 15, 22, 33, 40, 7]
# Even numbers : [10, 22, 40]
# Odd numbers : [15, 33, 7]
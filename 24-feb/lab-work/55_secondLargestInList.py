# Problem 55
# Problem Statement: Find second largest number in list.
# Input Format: Read input from standard input.
# Output Format: Print the required output.
# Constraints: Standard constraints apply.

n = int(input("Enter number of elements : "))
my_list = []
for i in range(n):
    element = int(input("Enter element : "))
    my_list.append(element)

largest = my_list[0]
second_largest = my_list[0]

for num in my_list:
    if num > largest:
        second_largest = largest
        largest = num
    elif num > second_largest and num != largest:
        second_largest = num

print("List :", my_list)
print("Second largest element is :", second_largest)

# output
# Enter number of elements : 5
# Enter element : 10
# Enter element : 25
# Enter element : 8
# Enter element : 42
# Enter element : 15
# List : [10, 25, 8, 42, 15]
# Second largest element is : 25
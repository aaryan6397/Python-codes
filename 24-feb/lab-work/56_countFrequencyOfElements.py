# Problem 56
# Problem Statement: Count frequency of elements in list.
# Input Format: Read input from standard input.
# Output Format: Print the required output.
# Constraints: Standard constraints apply.

n = int(input("Enter number of elements : "))
my_list = []
for i in range(n):
    element = int(input("Enter element : "))
    my_list.append(element)

print("List :", my_list)
print("Frequency of elements :")

counted = []
for item in my_list:
    if item not in counted:
        count = 0
        for num in my_list:
            if num == item:
                count += 1
        print(item, "->", count)
        counted.append(item)

# output
# Enter number of elements : 7
# Enter element : 1
# Enter element : 2
# Enter element : 3
# Enter element : 2
# Enter element : 1
# Enter element : 4
# Enter element : 1
# List : [1, 2, 3, 2, 1, 4, 1]
# Frequency of elements :
# 1 -> 3
# 2 -> 2
# 3 -> 1
# 4 -> 1
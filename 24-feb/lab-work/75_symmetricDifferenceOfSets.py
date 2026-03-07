# Problem 75
# Problem Statement: Find symmetric difference of two sets.
# Input Format: Read input from standard input.
# Output Format: Print the required output.
# Constraints: Standard constraints apply.

n1 = int(input("Enter number of elements in set 1 : "))
set1 = set()
for i in range(n1):
    element = int(input("Enter element : "))
    set1.add(element)

n2 = int(input("Enter number of elements in set 2 : "))
set2 = set()
for i in range(n2):
    element = int(input("Enter element : "))
    set2.add(element)

symmetric_diff = set1 ^ set2

print("Set 1 :", set1)
print("Set 2 :", set2)
print("Symmetric difference :", symmetric_diff)

# output
# Enter number of elements in set 1 : 4
# Enter element : 1
# Enter element : 2
# Enter element : 3
# Enter element : 4
# Enter number of elements in set 2 : 4
# Enter element : 3
# Enter element : 4
# Enter element : 5
# Enter element : 6
# Set 1 : {1, 2, 3, 4}
# Set 2 : {3, 4, 5, 6}
# Symmetric difference : {1, 2, 5, 6}
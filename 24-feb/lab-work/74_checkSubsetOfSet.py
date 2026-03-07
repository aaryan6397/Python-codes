# Problem 74
# Problem Statement: Check whether one set is subset of another.
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

print("Set 1 :", set1)
print("Set 2 :", set2)

is_subset = True
for item in set1:
    if item not in set2:
        is_subset = False
        break

if is_subset:
    print("Set 1 is a subset of Set 2")
else:
    print("Set 1 is not a subset of Set 2")

# output
# Enter number of elements in set 1 : 3
# Enter element : 1
# Enter element : 2
# Enter element : 3
# Enter number of elements in set 2 : 5
# Enter element : 1
# Enter element : 2
# Enter element : 3
# Enter element : 4
# Enter element : 5
# Set 1 : {1, 2, 3}
# Set 2 : {1, 2, 3, 4, 5}
# Set 1 is a subset of Set 2
# Q3: Find common elements between two lists using sets
# Input: list1 = [1, 2, 3, 4, 5], list2 = [4, 5, 6, 7, 8]
# Output: {4, 5}

list1 = [1, 2, 3, 4, 5]
list2 = [4, 5, 6, 7, 8]

set1 = set(list1)
set2 = set(list2)

common = set1.intersection(set2)

print("List 1:", list1)
print("List 2:", list2)
print("Common Elements:", common)

# Output:
# List 1: [1, 2, 3, 4, 5]
# List 2: [4, 5, 6, 7, 8]
# Common Elements: {4, 5}
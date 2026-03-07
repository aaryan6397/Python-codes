# union_set.py

# Take input for two sets
set1 = set(input("Enter first set: ").split())
set2 = set(input("Enter second set: ").split())

# Find union of the two sets using union() method
result = set1.union(set2)

# Print the union of the sets
print("Union:", result)



'''output:
Enter first set: 1 2 3
Enter second set: 3 4 5
Union: {'1', '2', '3', '4', '5'}
'''
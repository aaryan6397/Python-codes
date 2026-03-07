# Program to find common elements between two sets

# Take input for two sets
set1 = set(input("Enter first set numbers: ").split())
set2 = set(input("Enter second set numbers: ").split())

# Find common elements using intersection() method
common = set1.intersection(set2)
# Print common elements
print("Common Elements:", common)



'''output:
Enter first set numbers: 1 2 3 4
Enter second set numbers: 3 4 5 6
Common Elements: {'3', '4'}
'''

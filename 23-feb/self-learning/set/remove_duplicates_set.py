# remove_duplicates_set.py

# Take input of numbers separated by space
numbers_input = input("Enter numbers separated by space: ")
# Split the input string into a list of values and convert them to integers using  list comprehension 
values = numbers_input.split()
# Create a set to store unique numbers
numbers = []
# Convert input values to integers and add to the list
for v in values:
    numbers.append(int(v))
# Create a set of unique numbers
unique_numbers = set(numbers)
# Print unique numbers
print("Unique Numbers:", unique_numbers)


'''output:
Enter numbers separated by space: 1 2 3 2 4 1
Unique Numbers: {1, 2, 3, 4}
Enter numbers separated by space: 5 6 7 5 8 6
Unique Numbers: {8, 5, 6, 7}'''
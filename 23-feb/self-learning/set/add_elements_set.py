# add_elements_set.py

# Create an empty set
s = set()

# Take input for number of elements to add
n = int(input("How many elements? "))

for i in range(n):
    # Take input for element to add
    value = input("Enter element: ")
    # Add element to the set using add() method
    s.add(value
          )
# Print the set
print("Set:", s)



'''output:
How many elements? 4
Enter element: apple
Enter element: banana
Enter element: orange
Enter element: apple
Set: {'banana', 'orange', 'apple'}
'''
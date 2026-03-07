# WAP in python to create list of 20 numbers and ask the user to input any number and
# delete this number from the list from its all the occurences accept first occurence

numbersList = []


# we can also use list comprehension to create a list of 20 numbers

print("The list of numbers is: ", numbersList)
numToDelete = int(input("Enter number to delete from the list : "))
if(numToDelete != 0):
    frequency  = 0
    frequency = numbersList.count(numToDelete)
    if(frequency == 0):
        print("The number is not present in the list")
    elif(frequency == 1):
        print("The number is present only once in the list, so it cannot be deleted", numbersList)
    else:
        numbersList.reverse()
        for i in range(1,frequency):
            numbersList.remove(numToDelete)
        numbersList.reverse()
        print("The list after deletion of the number is: ", numbersList)
else:    
    print("Please enter a valid number to delete from the list")



'''output:
The list of numbers is:  [5, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 5,13, 14, 15, 16, 17, 18, 19, 20]
Enter number to delete from the list : 5
The list after deletion of the number is:  [2, 3, 4, 6, 7, 8, 9, 10, 11, 12,13, 14, 15, 16, 17, 18, 19, 20]
'''



# checking the type of set and list in python

# x = {}
# x.add(1)
# print(type(x))

'''output:
<class 'set'>
'''
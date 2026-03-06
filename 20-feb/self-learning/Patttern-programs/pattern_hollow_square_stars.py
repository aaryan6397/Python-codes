# File: pattern_hollow_square_stars.py
# Description: Print hollow square star pattern

rows = int(input("Enter size: "))

for i in range(rows):
    for j in range(rows):

        if i == 0 or i == rows-1 or j == 0 or j == rows-1:
            print("*", end=" ")
        else:
            print(" ", end=" ")

    print()



'''output:
Enter size: 5
* * * * * 
*       *
*       * 
*       * 
* * * * * 
'''

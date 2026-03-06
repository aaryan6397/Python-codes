# File: pattern_square_stars.py
# Description: Print square star pattern

rows = int(input("Enter size: "))

for i in range(rows):
    for j in range(rows):
        print("*", end=" ")
    print()



'''output:
Enter size: 5

* * * * * 
* * * * * 
* * * * * 
* * * * * 
* * * * * 

'''
# File: pattern_same_number_triangle.py
# Description: Print same number triangle pattern

rows = int(input("Enter rows: "))

for i in range(1, rows + 1):
    for j in range(i):
        print(i, end=" ")
    print()


'''output:
Enter rows: 5
1 
2 2
3 3 3 
4 4 4 4 
5 5 5 5 5 
'''

# pattern printing....


# first pattern..

# *
# **
# ***
# ****
# *****
# for i in range(1, 6):
#     print(" " * i)

  
#second pattern..

#
#      *
#     **
#    ***
#   ****
#  *****
# ******
# row = int(input("Enter rows : "))

# for i in range(row,0,-1):
#     print(" " * i, end="")
#     print("*" * (row - i + 1 ))



# third pattern..

#      *
#     ***
#    *****
#   *******
#  *********

# row = int(input("Enter rows : "))
# for i in range(row,0,-1):
#     print(" " * i, end="")
#     print("*" * (row - i + 1 ), end="")
#     print("*" * (row - i ))

# fourth pattern..


#      *
#     ***
#    *****
#   *******
#  *********
#   *******
#    *****
#     ***
#      *
# row = int(input("Enter rows : "))
# for i in range(row,0,-1):
#     print(" " * i, end="")
#     print("*" * (row - i + 1 ), end="")
#     print("*" * (row - i ))
# for i in range(2, row + 1):
#     print(" " * i, end="")
#     print("*" * (row - i + 1 ), end="")
#     print("*" * (row - i ))



#  fifth pattern..


# another star pattern
# *********
#  *******
#   *****
#    ***
#     *

row = int(input("Enter rows : "))
for i in range(row,0,-1):
    print(" " * (row - i), end="")
    print("*" * (2 * i - 1))  


    '''output:
    Enter rows : 5
    *********
     *******
      *****
       ***
        *
    '''
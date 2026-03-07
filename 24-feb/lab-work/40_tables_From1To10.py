# Problem 40
# Problem Statement: Print multiplication tables from 1 to 10.
# Input Format: Read input from standard input.
# Output Format: Print the required output.
# Constraints: Standard constraints apply.

for i in range(1, 11):
    print("Table of", i)
    for j in range(1, 11):
        print(i, "x", j, "=", i * j)
    print("-" * 10)

# Output:
# Table of 1
# 1 x 1 = 1 ... 1 x 10 = 10
# ----------
# Table of 2
# 2 x 1 = 2 ... 2 x 10 = 20
# ...
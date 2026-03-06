# Program: Convert seconds into hours, minutes, seconds

# input
total_seconds = int(input("Enter total seconds: "))

# calculation
hours = total_seconds // 3600
minutes = (total_seconds % 3600) // 60
seconds = total_seconds % 60

# output
print("Time =", hours, "hours", minutes, "minutes", seconds, "seconds")


'''output:
Enter total seconds: 3665
Time = 1 hours 1 minutes 5 seconds
'''
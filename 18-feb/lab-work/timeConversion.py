# this program converts time in seconds to hours, minutes and seconds. It will take time in seconds as input from the user and then calculate the hours, minutes and seconds using the formula.
#  The program will also check if the time in seconds is greater than 0 before calculating the hours, minutes and seconds.

# Enter time in seconds
seconds =  int(input("Enter time in seconds : "))

# initializing no of hours and minutes
minutes = 0
hours = 0


# calculate hours
if(seconds >= 3600):
    hours = seconds // 3600 #storing quotient as hours
    seconds = seconds % 60 #storing reminder as seconds

# calculate minutes
if(seconds >= 60):
    minutes = seconds // 60 #storing quotient as minutes
    seconds = seconds % 60 #storing reminder as seconds

# output
# print("Time in hours : ", hours)
# print("Time in minutes : ", minutes)
# print("Time in seconds : ", seconds)

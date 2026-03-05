#4. Salary Increment System An employee’s increment depends on: 
# • Performance rating (1–5) 
# • Years of experience
# • Attendance percentage 
# Design logic to calculate increment percentage based on these factors.



# employee inputs
rating = int(input("Enter performance rating (1-5): "))
experience = int(input("Enter years of experience: "))
attendance = float(input("Enter attendance percentage: "))

increment = 0

# performance based increment
if rating >= 4:
    increment = 10
elif rating == 3:
    increment = 7
else:
    increment = 3

# experience bonus
if experience > 5:
    increment += 3

# attendance bonus
if attendance > 90:
    increment += 2

print("Total Increment Percentage:", increment, "%")


'''output:
Enter performance rating (1-5): 4
Enter years of experience: 6
Enter attendance percentage: 95
Total Increment Percentage: 15 %    
'''

# WAP in python to create a attendance tracker for a class of 30 students and calculate the percentage of attendance and also give a warning if the percentage is below 75% and also replace the consecutive absences with "Warning" in the list.
# we can also use list comprehension to create a list of 30 students attendance

# enter attendance as 1 for present and 0 for absent
attendance_input = input("Enter attendance (1=Present, 0=Absent): ")

# convert the input string to a list of integers
attendance = []
for value in attendance_input.split():
    attendance.append(int(value))
    
percentage = (sum(attendance) / len(attendance)) * 100
print("Attendance Percentage:", percentage)

if percentage < 75:
    print("Warning: Below 75% attendance")

# Replace consecutive absences
for i in range(len(attendance)-1):
    if attendance[i] == 0 and attendance[i+1] == 0:
        attendance[i] = "Warning"

print("Updated Attendance:", attendance)



'''output:
Enter attendance (1=Present, 0=Absent): 1 0 1 0 0 1 1 0 1 1 1 0 0 1 1 1 0 0 1 1 1 0 0 1 1 1 0 0 1
Attendance Percentage: 60.0
Warning: Below 75% attendance   
Updated Attendance: [1, 0, 1, 'Warning', 1, 1, 0, 1, 1, 1, 0, 'Warning', 1, 1, 1, 0, 'Warning', 1, 1, 1, 0, 'Warning', 1]

'''
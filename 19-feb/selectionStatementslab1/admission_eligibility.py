#4. University Admission Eligibility A student applies for admission. Eligibility rules: 
# • Minimum 75% in 12th grade 
# • Must have studied Mathematics
# • Entrance exam score ≥ 80
#  If any condition fails, show the exact reason.



# 12th percentage input
percentage = float(input("Enter 12th percentage: "))

# mathematics subject check
maths = input("Did you study Mathematics? (yes/no): ")

# entrance exam score input
exam_score = int(input("Enter entrance exam score: "))

# eligibility conditions check
if percentage < 75:
    print("Not eligible: Minimum 75% required in 12th grade.")
elif maths.lower() != "yes":
    print("Not eligible: Mathematics subject is required.")
elif exam_score < 80:
    print("Not eligible: Entrance exam score must be at least 80.")
else:
    print("Student is eligible for admission.")

'''output:
Enter 12th percentage: 78
Did you study Mathematics? (yes/no): yes
Enter entrance exam score: 85   
Student is eligible for admission.

Enter 12th percentage: 72
Did you study Mathematics? (yes/no): yes
Enter entrance exam score: 90
Not eligible: Minimum 75% required in 12th grade.

Enter 12th percentage: 80
Did you study Mathematics? (yes/no): no
Enter entrance exam score: 85
Not eligible: Mathematics subject is required.

Enter 12th percentage: 82
Did you study Mathematics? (yes/no): yes
Enter entrance exam score: 75
Not eligible: Entrance exam score must be at least 80.'''



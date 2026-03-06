# Program: Calculate student grade based on marks

# input
marks = int(input("Enter marks: "))

# grading logic
if marks >= 90:
    print("Grade: A")
elif marks >= 75:
    print("Grade: B")
elif marks >= 60:
    print("Grade: C")
elif marks >= 40:
    print("Grade: D")
else:
    print("Grade: Fail")


'''output:
Enter marks: 85
Grade: B
'''
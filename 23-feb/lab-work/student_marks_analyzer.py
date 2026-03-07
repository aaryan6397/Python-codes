marks = list(map(int, input("Enter student marks separated by space: ").split()))

# Remove invalid marks
valid_marks = []
for m in marks:
    if 0 <= m <= 100:
        valid_marks.append(m)

if len(valid_marks) == 0:
    print("No valid marks entered.")
else:
    avg = sum(valid_marks) / len(valid_marks)
    topper = max(valid_marks)

    print("Average:", avg)
    print("Topper Marks:", topper)

    if avg >= 90:
        print("Grade: A")
    elif avg >= 75:
        print("Grade: B")
    elif avg >= 50:
        print("Grade: C")
    else:
        print("Grade: Fail")


'''output:
Enter student marks separated by space: 85 90 78 92 88
Average: 86.6
Topper Marks: 92
Grade: A

Enter student marks separated by space: 45 55 60 70 80
Average: 62.0
Topper Marks: 80
Grade: C

Enter student marks separated by space: 30 40 50 60 70
Average: 50.0
Topper Marks: 70
Grade: C

Enter student marks separated by space: 20 30 40 50 60
Average: 40.0
Topper Marks: 60
Grade: Fail

Enter student marks separated by space: 110 -5 95 85 75
Average: 85.0
Topper Marks: 95
Grade: A

'''
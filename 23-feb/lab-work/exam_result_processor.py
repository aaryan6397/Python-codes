
# WAP in python to create a exam result processor that takes a list of student scores as input and removes the lowest two scores, adds grace marks to the scores between 30 and 35, and counts the number of students who passed (score >= 40).
# enter student scores as space separated values, for example: 25 30 35 40 45 50
score_input = input("Enter student scores separated by space: ")

values = score_input.split()
scores = []

# Convert to integers
for v in values:
    scores.append(int(v))

# Remove lowest score (first time)
lowest_index = 0
for i in range(len(scores)):
    if scores[i] < scores[lowest_index]:
        lowest_index = i

scores.pop(lowest_index)

# Remove lowest score (second time)
lowest_index = 0
for i in range(len(scores)):
    if scores[i] < scores[lowest_index]:
        lowest_index = i

scores.pop(lowest_index)

# Add grace marks
for i in range(len(scores)):
    if scores[i] >= 30 and scores[i] <= 35:
        scores[i] = scores[i] + 5

# Count passed students
passed = 0
for i in range(len(scores)):
    if scores[i] >= 40:
        passed = passed + 1

print("Passed Students:", passed)




'''output:
    Enter student scores separated by space: 25 30 35 40 45 50
    Passed Students: 4
    Enter student scores separated by space: 20 25 30 35 40 45
    Passed Students: 3
    
'''
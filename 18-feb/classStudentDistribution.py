#this program will calculate how many classes we need to accommodate 125 students if each class can have a maximum of 30 students. 
# It will also calculate how many students will remain without a class.

students = 125
eachClassHaveStudentes = 30

totalClass = students // eachClassHaveStudentes
remainStudents = students %  eachClassHaveStudentes

print("total class : ",totalClass)
print("remains students : ",remainStudents)

'''output:
total class :  4
remains students :  5
'''
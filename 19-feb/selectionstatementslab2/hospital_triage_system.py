'''3. Hospital Emergency Triage Patients are categorized as:
• Critical (heart rate abnormal OR severe injury) 
• Moderate 
• Normal
If age > 65 and condition is moderate → Upgrade priority.'''



# patient details input
age = int(input("Enter patient age: "))
heart_rate = int(input("Enter heart rate: "))
injury = input("Severe injury? (yes/no): ")

# condition evaluation
if heart_rate < 60 or heart_rate > 100 or injury.lower() == "yes":
    category = "Critical"
elif 60 <= heart_rate <= 100:
    category = "Moderate"
else:
    category = "Normal"

# priority upgrade for elderly
if age > 65 and category == "Moderate":
    category = "Critical"

print("Patient Priority Category:", category)


'''output:

Enter patient age: 70
Enter heart rate: 80 
Severe injury? (yes/no): no
Patient Priority Category: Critical

Enter patient age: 30
Enter heart rate: 90
Severe injury? (yes/no): no
Patient Priority Category: Moderate'''
'''1. Electricity Bill Calculator Calculate the electricity bill based on units consumed: 
 • 0–100 → ₹5/unit
 • 101–300 → ₹7/unit
 • Above 300 → ₹10/unit 
If the user is a senior citizen, apply 10% discount.'''



# units consumed input
units = float(input("Enter electricity units consumed: "))

# senior citizen check
senior = input("Are you a senior citizen? (yes/no): ")

bill = 0

# slab calculation
if units <= 100:
    bill = units * 5
elif units <= 300:
    bill = (100 * 5) + (units - 100) * 7
else:
    bill = (100 * 5) + (200 * 7) + (units - 300) * 10

# senior citizen discount
if senior.lower() == "yes":
    bill = bill * 0.90   # 10% discount

print("Total Electricity Bill: ₹", bill)



'''output:

Enter electricity units consumed: 350
Are you a senior citizen? (yes/no): yes
Total Electricity Bill: ₹ 3150.0


'''
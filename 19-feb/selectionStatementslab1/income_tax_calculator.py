# 2. Income Tax Calculator (India Based) Create a program that calculates income tax based on the following slabs:
#  • Up to ₹2,50,000 → No tax 
# • ₹2,50,001 – ₹5,00,000 → 5% 
# • ₹5,00,001 – ₹10,00,000 → 20% 
# • Above ₹10,00,000 → 30% 
# Additionally, if the person is a senior citizen (age ≥ 60),increase the exemption limit to ₹3,00,000.


# user se annual income lena
income = float(input("Enter your annual income: "))

# user ki age lena
age = int(input("Enter your age: "))

# default exemption limit
exemption = 250000

# agar senior citizen hai to exemption badh jayega
if age >= 60:
    exemption = 300000

# tax variable initialize karna
tax = 0

# tax slab conditions
if income <= exemption:
    tax = 0  # exemption tak koi tax nahi
elif income <= 500000:
    tax = (income - exemption) * 0.05  # 5% tax
elif income <= 1000000:
    tax = (500000 - exemption) * 0.05 + (income - 500000) * 0.20  # 20% slab
else:
    tax = (500000 - exemption) * 0.05 + (1000000 - 500000) * 0.20 + (income - 1000000) * 0.30  # 30%

# final tax print karna
print("Total Tax:", tax)

'''output:
Enter your annual income: 750000
Enter your age: 45
    
    Total Tax: 37500.0'''
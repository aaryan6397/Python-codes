#3. E-commerce Discount Engine An online shopping platform gives discounts based on: 
# • Cart value
# • Customer membership (Silver/Gold/Platinum) 
# • Festival season 
# Apply the highest eligible discount and print the final payable amount.

# cart value input
cart = float(input("Enter cart value: "))

# customer membership input
membership = input("Enter membership (Silver/Gold/Platinum): ")

# festival season check
festival = input("Is it festival season? (yes/no): ")

# discount variable
discount = 0

# membership ke basis par discount
if membership.lower() == "silver":
    discount = 5
elif membership.lower() == "gold":
    discount = 10
elif membership.lower() == "platinum":
    discount = 15

# festival season me special discount
if festival.lower() == "yes":
    discount = max(discount, 20)

# final payable amount calculate karna
final_amount = cart - (cart * discount / 100)

# output show karna
print("Discount applied:", discount, "%")
print("Final payable amount:", final_amount)
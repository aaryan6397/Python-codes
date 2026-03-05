#5. ATM Withdrawal System Conditions: 
#  • Account balance must be sufficient
#  • Daily withdrawal limit ₹50,000
#  • ATM cash availability 
# Display appropriate messages for each condition failure.

# account details input
balance = float(input("Enter account balance: "))
withdraw = float(input("Enter withdrawal amount: "))
atm_cash = float(input("Enter ATM available cash: "))

daily_limit = 50000

# condition checks
if withdraw > balance:
    print("Transaction failed: Insufficient account balance.")
elif withdraw > daily_limit:
    print("Transaction failed: Exceeds daily withdrawal limit.")
elif withdraw > atm_cash:
    print("Transaction failed: ATM does not have enough cash.")
else:
    balance -= withdraw
    print("Withdrawal successful.")
    print("Remaining balance:", balance)

'''output:
Enter account balance: 100000
Enter withdrawal amount: 60000
Enter ATM available cash: 70000
Transaction failed: Exceeds daily withdrawal limit.
'''
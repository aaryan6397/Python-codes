''' 1. Banking – Suspicious Transaction Detection 
    A bank wants to flag suspicious transactions. •
      If the transaction amount is greater than ₹2,00,000 • 
      And the account is less than 6 months old • 
      And the transaction is international Write a program to detect whether the transaction should be flagged for manual verification.'''

# user se transaction amount lena
amount = float(input("Enter transaction amount: "))

# account kitne months purana hai
account_age = int(input("Enter account age in months: "))

# kya transaction international hai
international = input("Is the transaction international? (yes/no): ")

# condition check karna suspicious transaction ke liye
if amount > 200000 and account_age < 6 and international.lower() == "yes":
    # agar teeno conditions true hain
    print("Transaction flagged for manual verification.")
else:
    # agar suspicious nahi hai
    print("Transaction is normal.")


    '''output:
Enter transaction amount: 250000    
Enter account age in months: 4
Is the transaction international? (yes/no): yes
Transaction flagged for manual verification.

Enter transaction amount: 150000
Enter account age in months: 8
Is the transaction international? (yes/no): no

Transaction is normal.

Enter transaction amount: 300000
Enter account age in months: 3
Is the transaction international? (yes/no): no'''
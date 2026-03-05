#5. Loan Approval System Loan approval depends on: 
#  • Credit score 
#  • Monthly income 
#  • Existing loan amount Rules:
#  • Credit score < 600 → Reject
#  • 600–750 → Further check income 
#  • 750 → Approve
#If income < ₹30,000 and existing loans > ₹5,00,000 → Reject.



# credit score input
credit_score = int(input("Enter credit score: "))

# monthly income input
income = float(input("Enter monthly income: "))

# existing loan amount input
existing_loan = float(input("Enter existing loan amount: "))

# credit score conditions
if credit_score < 600:
    print("Loan Rejected: Low credit score.")
elif credit_score >= 750:
    print("Loan Approved.")
else:
    # further check for income and existing loan
    if income < 30000 and existing_loan > 500000:
        print("Loan Rejected: Low income and high existing loan.")
    else:
        print("Loan under review.")

'''output:

# first case: low credit score

Enter credit score: 580
Enter monthly income: 25000
Enter existing loan amount: 600000
Loan Rejected: Low credit score.


# second case: good credit score

Enter credit score: 760
Enter monthly income: 40000
Enter existing loan amount: 200000
Loan Approved.

# third case: loan under review

Enter credit score: 700
Enter monthly income: 25000
Enter existing loan amount: 300000
Loan under review.

# fourth case: borderline credit score but low income and high existing loan

Enter credit score: 700
Enter monthly income: 25000
Enter existing loan amount: 600000
Loan Rejected: Low income and high existing loan.'''

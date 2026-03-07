# WAP in python to create a bank transaction analyzer that takes a list of transactions as input and calculates the total balance, largest withdrawal, and number of deposits greater than 10000.


# enter transactions as space separated values, for example: 1000 -500 2000 -300 15000
transaction_input = input("Enter transactions separated by space: ")

transactions = []
values = transaction_input.split()

for v in values:
    transactions.append(int(v))

balance = 0
largest_withdrawal = 0
large_deposits = 0

for t in transactions:
    balance = balance + t

    if t < 0:
        if largest_withdrawal == 0 or t < largest_withdrawal:
            largest_withdrawal = t

    if t > 10000:
        large_deposits = large_deposits + 1

print("Total Balance:", balance)
print("Largest Withdrawal:", largest_withdrawal)
print("Deposits > 10000:", large_deposits)



'''output:
Enter transactions separated by space: 1000 -500 2000 -300 15000
Total Balance: 16500
Largest Withdrawal: -500
Deposits > 10000: 1
'''


'''output:

Enter transactions separated by space: 5000 -2000 3000 -1000 12000
Total Balance: 14000
Largest Withdrawal: -2000
Deposits > 10000: 1'''
# this program will calculate the total bill for a shopping trip based on the number of books and pens purchased. The price of each book is 45 and the price of each pen is 20. 
# The program will then ask the user to enter the amount they are paying and will calculate the remaining balance if the payment is less than the total bill. 
# If the payment is equal to the total bill, it will thank the user for their payment.


# Enter the number of books you buy: 2
books = int(input("Enter the number of books you buy: "))
# Enter the number of pens you buy: 3
pens = int(input("Enter the number of pens you buy: "))
# The price of each book is 45 and the price of each pen is 20.
bookPrice = 45
penPrice = 20

#total bill for a shopping trip based on the number of books and pens purchased
totalBill = (books * bookPrice) + (pens * penPrice)
# Enter the amount they are paying
payment = int(input("Enter the amount you pay: "))

#condition to check if the payment is  equal to the total bill, it will thank the user for their payment. 

if(payment == totalBill):
    print("Thank you for your payment. Your bill is paid in full.")
else:
    remainingAmount = totalBill - payment
    print("Thank you for your payment. Your remaining balance is: ", remainingAmount)

'''output:
Enter the number of books you buy: 2
Enter the number of pens you buy: 3
Enter the amount you pay: 100
Thank you for your payment. Your remaining balance is:  35
'''
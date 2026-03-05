# this program calculates the profit or loss of a product based on the cost price and sell price entered by the user.
# The program will first check if the cost price and sell price are positive numbers. If they are not, it will print an error message and exit the program. 
# If they are valid, it will then calculate the profit or loss and print the result. If there is no profit or loss, it will print "No profit No loss".


# Enter cost price (in RS)
cost_price = float(input("Enter cost price (in RS) : "))

# Check if the cost price is positive
if(cost_price <= 0):
    print("cost Price should be positive")
    # exit the program if the cost price is not positive
    exit()
else:
    # Enter sell price (in RS)
    sell_price = float(input("Enter sell price : (in RS) "))
    if(sell_price <= 0):
        print("sell Price should be positive")
        # exit the program if the sell price is not positive
        exit()
    else:
        #check if the cost price is greater than the sell price
        if(cost_price > sell_price):
            #print the loss and the amount of loss
            print("loss", cost_price - sell_price)
            # exit the program after calculating the loss
            exit()
        #check if the cost price is less than the sell price
        elif(cost_price < sell_price):
            #print the profit and the amount of profit
            print("profit", sell_price - cost_price)
            # exit the program after calculating the profit
            exit()
        #check if the cost price is equal to the sell price
        else:
            #print the  result
            print("No profit No loss")


'''output:
Enter cost price (in RS) : 100
Enter sell price : (in RS) 150
profit 50.0
'''  
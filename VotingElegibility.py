try:
    age = int(input("Enter your age: "))

    if age < 0:
        print("Invalid age entered.")

    elif age >= 18:
        print("Eligible for Voting")

    else:
        print("Not Eligible for Voting")

except ValueError:
    print("Error: Please enter a valid numeric age.")

except Exception as e:
    print("Unexpected Error:", e)
# Problem 7
# Problem Statement: Convert temperature from Fahrenheit to Celsius.
# Input Format: Read input from standard input.
# Output Format: Print the required output.
# Constraints: Standard constraints apply.


# Read temperature in Fahrenheit from user input
Fahrenheit = float(input("Enter the temprature in Fahrenheit : ")) 
# Convert Fahrenheit to Celsius using the formula: C = (F - 32) * 5/9
Celsius = (Fahrenheit - 32)  * 5/9
# Print the temperature in Celsius
print("Temperature in Celsius:", Celsius)

# output
# Enter the temprature in Fahrenheit : 37
# Temperature in Celsius: 98.6
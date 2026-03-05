# this program will calculate the area and parameter of a circle. It will take the radius as input from the user and then calculate the area and parameter using the formula. 
# The program will also check if the radius is greater than 0 before calculating the area and parameter.

# Enter the radius of the circle
radius = float(input("Enter the radius (in centimeter) :  "))

# Check if the radius is greater than 0
if(radius <= 0.0):
    print("radius should be greater then 0.0")
    exit()
else:
    pie = 3.14
    area = 0
    parameter = 0
    area = pie * radius * radius
    parameter = 2 * pie * radius
    print("area of circle",area)
    print("area of parameter",parameter)

'''output:
Enter the radius of the circle: 5
area of circle 78.5
area of parameter 31.400000000000002
'''
     
# This program will check if the angles entered by the user can form a triangle or not. 
# It will take three angles as input from the user and then check if the sum of the angles is equal to 180 degrees. 
# If the sum is equal to 180 degrees, then it will print "This is triangle", otherwise it will print "Not triangle". 
# The program will also check if the angles are positive before checking if they can form a triangle or not. 

# Enter the right angle
right_angle = int(input("Enter the right angle: "))
# Check if the angles are positive before checking if they can form a triangle or not.
if(right_angle <= 0):
    print("angle should be positive")
# exit the program if the angle is not positive
    exit()
else:
    # Enter the left angle
    left_angle = int(input("Enter the left angle: "))
    # Check if the angles are positive before checking if they can form a triangle or not.
    if(left_angle < 0):
        print("angle should be positive")
        # exit the program if the angle is not positive
        exit()
    else:
        # Enter the bottom angle
        bottom_angle = int(input("Enter the bottom angle: "))
        # Check if the angles are positive before checking if they can form a triangle or not.
        if(bottom_angle < 0):
            print("angle should be positive")
            # exit the program if the angle is not positive
            exit()
        else:
            # check if the sum of the angles is equal to 180 degrees.
            if(right_angle + left_angle + bottom_angle == 180):
                # print the result
                print("This is triangle")
            else:
                # print the result
                print("Not triangle")

# angle_total = right_angle + left_angle + bottom_angle

'''output:
Enter the right angle: 60
Enter the left angle: 60
Enter the bottom angle: 60
This is triangle'''


import math
import threedifigures as tf

r = float(input("Enter radius of cone: "))
h = float(input("Enter height of cone: "))

# Slant height calculation
l = math.sqrt(r*r + h*h)

print("Curved Surface Area:", tf.cone_csa(r, l))
print("Total Surface Area:", tf.cone_tsa(r, l))
print("Volume:", tf.cone_volume(r, h))



'''output:
Enter radius of cone: 3
Enter height of cone: 4
Curved Surface Area: 37.69911184307752
Total Surface Area: 65.97344572538566
Volume: 37.69911184307752
'''
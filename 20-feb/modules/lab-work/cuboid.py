import threedifigures as tf

l = float(input("Enter length of cuboid: "))
b = float(input("Enter breadth of cuboid: "))
h = float(input("Enter height of cuboid: "))

print("Curved Surface Area:", tf.cuboid_csa(l, b, h))
print("Total Surface Area:", tf.cuboid_tsa(l, b, h))
print("Volume:", tf.cuboid_volume(l, b, h))


'''output:
Enter length of cuboid: 5
Enter breadth of cuboid: 3
Enter height of cuboid: 4
Curved Surface Area: 56.0
Total Surface Area: 94.0
Volume: 60.0
'''


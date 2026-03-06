import threedifigures as tf

r = float(input("Enter radius of cylinder: "))
h = float(input("Enter height of cylinder: "))

print("Curved Surface Area:", tf.cylinder_csa(r, h))
print("Total Surface Area:", tf.cylinder_tsa(r, h))
print("Volume:", tf.cylinder_volume(r, h))


'''output:
Enter radius of cylinder: 3
Enter height of cylinder: 5
Curved Surface Area: 94.247
Total Surface Area: 150.7964
Volume: 141.371
'''
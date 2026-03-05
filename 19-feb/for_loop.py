
# simple loop

for n in range(10,30,4):
    print(n*2,end=",")

# natural numbers
for n in range(1,21):
     print(n,end=",")

# sum of natural numbers

#initializing sum variable equal to 0
Sum = 0
for n in range(1,21):  
    Sum += n
print("sum of first 20 natural numbers : ",Sum)



'''output:


# simple loop results
20,28,36,44,52,60,68,76,84,92,

# natural numbers results
1,2,3,4,5,6,7,8,9,10

# sum of natural numbers results
11,12,13,14,15,16,17,18,19,20,
sum of first 20 natural numbers :  210'''


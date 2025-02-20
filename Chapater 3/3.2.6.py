############### 2 is initial and 8 is limit and 3 is increment ########################

for i in range (2, 20, 3):
    print("The value of i is: ", i)

# Do not execute the code because the starting and final is same
for i in range(1, 1):
    print("The value of i is currently", i)

for i in range(2, 1):
    print("The value of i is currently", i)

######################

power = 1
for num in range(20):
    print("2 to the power of", num, "is", power)
    power *= 2
#The break and continue statement

#break-example

print ("The break instruction: ")
for i in range(1, 6):
    if i == 3:
        break
    print(f"Inside the loop: {i}")
print(f"Outside the loop")

#continue_example

print("\nThe continue instruction: ")
for i in range(1, 6):
    if i == 3:
        continue
    print(f"Inside the loop: {i}")
print(f"Outside the loop")


####

largest_num = -99999999
counter = 0
while True:
    num = int(input("Enter a number: "))
    if num == -1:
        break
    counter += 1
    if num > largest_num:
        largest_num = num

if counter != 0:
    print(f"The largest number is: {largest_num}")

else:
    print("You haven't entered any numbers.")



largest_number = -9999999
counter = 0

num = int(input("Enter a number: "))

while num != -1:
    if num == -1:
        continue
    counter += 1

    if num > largest_number:
        largest_number = num
    num = int(input("Enter a number: "))

if counter:
    print("The largest number is: ", largest_number)
else:
    print("You haven't entered any numbers.")

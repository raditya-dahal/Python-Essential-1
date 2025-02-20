secret_num = 777

user_number = int(input("Enter the number: "))

while user_number != secret_num:
    print("Ha ha! You are stucked in a loop!")

    user_number = int(input("Enter the number: "))

print(user_number)
print("Well done, muggle! You are free now.")


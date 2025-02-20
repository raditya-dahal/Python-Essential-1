# while True:
#     print("I'm stuck inside a loop.")


large_num = -999999

num = int(input("Enter a number: "))

while num != -1:
    if num > large_num:
        large_num = num

    num = int(input("Enter a number: "))

print(large_num)

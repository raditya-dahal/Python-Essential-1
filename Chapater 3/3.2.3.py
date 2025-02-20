""" A program that reads a sequence of numbers and counts how many numbers are even and how many are odd.
The program terminates when zero is entered."""

odd_num = 0
even_num = 0

num = int(input("Enter a number or type 0 to stop: "))

while num != 0:

    if num % 2 == 1:
        odd_num += 1

    else:
        even_num += 1

    num = int(input("Enter a number or type 0 to stop: "))

print("odd_count: ", odd_num)
print("even_count: ", even_num)

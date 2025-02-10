#
# #_____The input() Function
# print("Tell me Anything")
# anything = input()
# print(anything)
#
# #_____The input function with an argument
#
# anyThing = input("Tell me something: ")
# print("Anything..",anyThing, "really?")
#
#
# #______The result of the input() Function
# """any_thing = input("Enter a number: ")
# something = any_thing ** 2.0
# print(anything, "to the power of 2 is", something)  #Error due to operators"""
#
#
# #_______Using int or float to the above type of problem
#
# number = float(input("Enter a number: "))
# power = number ** 2
# print(number, "to the power of 2 is: ", power)
#
#
# #Calculate the hypothesis using input
#
# length_a = float(input("Enter a length: "))
# length_b = float(input("Enter a length: "))
# hypo = (length_a ** 2 + length_b **2) ** 0.5
# print(hypo)
# print("Hypotenus is: ", round(hypo, 2))  #round and 2 will round off with 2 digit after decimal
#
# # you can remove variable as well by directly entering the length with formula
#
# print("Hypo is: ", (length_a**2 + length_b**2)**.5)
#
#
#
# #__________String Operators________
# # + sign to be a concatenator,
# fName = input("Enter First Name: ")
# lName = input("Enter Last Name: ")
# print("Thank You!")
# print("\nYour Name is "+ fName + " " + lName + ".")
#
# #  * gives to number and string is replication
#
# print("+" + 10 * "-" + "+")
# print(("|" + " " * 10 + "|\n") * 5, end="")
# print("+" + 10 * "-" + "+")
# ____________________________________________________________________________________________________
# #Printing all add, sub, mul and div with float input a and b
#
# a = float(input("Enter the number a: "))
# b = float(input("Enter the number b: "))
#
# add = a + b
# sub = a - b
# mul = a * b
# div = a / b
#
# print("\n All Addition, subtraction, multiplication and Division are: ","\n", add,"\n",sub,"\n", mul,"\n", div)
#
# #Solution from Cisco
# a = float(input("Enter first value: "))
# b = float(input("Enter second value: "))
# print("Addition:", a + b)
# print("Subtraction:", a - b)
# print("Multiplication:", a * b)
# print("Division:", a / b)
# print("\nThat's all, folks!")


a = (796%60)
print(a)
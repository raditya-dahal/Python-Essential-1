income = float(input("Enter Annual income: "))

if income < 85525:
    tax = income * 0.18 - 556.02

else:
    tax = (income - 85528) * 0.32 + 14839.02

if tax < 30000:
    tax = 0

tax = round (tax, 2)
print ("Your tax is: ", tax, "Tharels")

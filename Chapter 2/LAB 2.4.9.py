"""Scenario
Miles and kilometers are units of length or distance.

Bearing in mind that 1 mile is equal to approximately 1.61 kilometers,
complete the program in the editor so that it converts:

miles to kilometers;
kilometers to miles.
Do not change anything in the existing code. Write your code in the places indicated by ###.
Test your program with the data we've provided in the source code.

Pay particular attention to what is going on inside the print() function.
Analyze how we provide multiple arguments to the function, and how we output the expected data.

Note that some of the arguments inside the print() function are strings (e.g., "miles is",
whereas some other are variables (e.g., miles).

  Tip
There's one more interesting thing happening there. Can you see another function inside the print() function?
It's the round() function. Its job is to round the outputted result to the number of decimal places specified in
the parentheses, and return a float (inside the round() function you can find the variable name, a comma,
and the number of decimal places we're aiming for). We're going to talk about functions very soon,
so don't worry that everything may not be fully clear yet. We just want to spark your curiosity"""

kilometers = 12.25
miles = 7.38

miles_to_kilometers = miles * 1.61
kilometers_to_miles = kilometers / 1.61

print(miles, "miles is", round(miles_to_kilometers, 2),
      "kilometers")  # round will round off and 2 means up to 2 int after decimal
print(kilometers, "kilometers is", round(kilometers_to_miles, 8), "miles")


print()
#USD to Euro

usd = float(input("Enter USD: "))
rate = 0.96
euro = usd * rate
print("Euro is:", round(euro, 2))

print()
#temperature

celsius = float(input("Enter Celsius: "))
fahrenheit = celsius * 1.8
print("Fahrenheit is: ", round(fahrenheit, 2))

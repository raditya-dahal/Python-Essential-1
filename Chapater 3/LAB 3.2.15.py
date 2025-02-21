c0 = int(input("Enter a natural number: "))  # Read input
steps = 0  # Initialize step counter

if c0 <= 0:
    print("Please enter a positive integer.")
else:
    while c0 != 1:  # Loop until c0 becomes 1
        print(c0)  # Print the current value
        if c0 % 2 == 0:  # If c0 is even
            c0 = c0 // 2
        else:  # If c0 is odd
            c0 = 3 * c0 + 1
        steps += 1  # Count steps

    print(c0)  # Print final 1
    print("Steps:", steps)  # Print step count

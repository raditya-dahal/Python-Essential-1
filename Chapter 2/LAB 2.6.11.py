hour = int(input("Starting time (hours): "))
mins = int(input("Starting time (minutes): "))
dura = int(input("Event duration (minutes): "))


# Calculate total minutes from the start of the day
total_mins = hour * 60 + mins + dura

# Compute the new hour and minutes using modulus
end_hour = (total_mins // 60) % 24  # Ensure it wraps around 24 hours
end_mins = total_mins % 60

print(f"End time: {end_hour:02}:{end_mins:02}")


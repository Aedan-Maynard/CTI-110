#Aedan Maynard
#10/27/24
#P3LAB
#Money Calculation

# Get user input
amount = float(input("Enter the amount of money (e.g., 5.67): "))

# Convert amount to cents
total_cents = int(amount * 100)

# Calculate the number of each type of coin
dollars = total_cents // 100
total_cents %= 100  # Remaining cents after extracting dollars

quarters = total_cents // 25
total_cents %= 25  # Remaining cents after extracting quarters

dimes = total_cents // 10
total_cents %= 10  # Remaining cents after extracting dimes

nickels = total_cents // 5
total_cents %= 5  # Remaining cents after extracting nickels

pennies = total_cents  # Remaining cents are all pennies

# Display results
if dollars > 0:
    print(f"{dollars} dollar{'s' if dollars > 1 else ''}")

if quarters > 0:
    print(f"{quarters} quarter{'s' if quarters > 1 else ''}")

if dimes > 0:
    print(f"{dimes} dime{'s' if dimes > 1 else ''}")

if nickels > 0:
    print(f"{nickels} nickel{'s' if nickels > 1 else ''}")

if pennies > 0:
    print(f"{pennies} penn{'ies' if pennies > 1 else 'y'}")

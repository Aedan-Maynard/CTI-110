# Aedan Maynard
# 10/13/24
# P2HW2
# String Formating

# Step 3: Ask user to enter their budget
budget = float(input("Enter your budget for the trip: "))

# Step 4: Ask user to enter travel destination
destination = input("Enter your travel destination: ")

# Step 5: Ask user for amount they will spend on gas
gas_expense = float(input("Enter the amount you will spend on gas: "))

# Step 6: Ask user for amount they will spend on accommodation
accommodation_expense = float(input("Enter the amount you will spend on accommodation: "))

# Step 7: Ask user for amount they will spend on food
food_expense = float(input("Enter the amount you will spend on food: "))

# Step 8: Add expenses
total_expenses = gas_expense + accommodation_expense + food_expense

# Step 9: Subtract expenses from budget
remaining_budget = budget - total_expenses

# Step 10: Display Results

print(f"\n{'Travel Destination:':<25} {destination}")
print(f"{'Total Expenses:':<25} ${total_expenses:.2f}")
print(f"{'Remaining Budget:':<25} ${remaining_budget:.2f}")

if remaining_budget < 0:
    print("You are over budget!")
else:
    print("You are within your budget.")

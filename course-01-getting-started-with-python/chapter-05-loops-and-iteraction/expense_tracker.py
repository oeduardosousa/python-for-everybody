# Expense Tracker

expense = 0
count = 0

# Get user input for budget and expenses
budget = float(input("Enter your budget: "))
decision = input("Do you want to enter an expense? (yes/no): ")
# Loop to track expenses
while decision.lower() == "yes":
    amount = float(input("Enter the expense amount: "))
    if expense + amount <= budget:
        expense += amount
        count += 1
    else:
        # When the expense exceeds the budget, display a message and break the loop
        print("Expense exceeds budget.")
        break
    # Ask user if they want to enter another expense
    decision = input("Do you want to enter another expense? (yes/no): ")

# Display total expenses and amount
print(f"Total expenses: {count}")
print(f"Total amount: {expense}")
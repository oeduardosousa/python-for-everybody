#Monthly Savings Calculator

#Receive user input for monthly savings and number of months
save = float(input("How much do you want to save each month? "))
months = float(input("How many months will you save? "))

#Calculate total savings
total_saved = save * months

#Display the total savings
print("Total amount saved after", months, "months is:", total_saved)
print("Total saves: ", total_saved)
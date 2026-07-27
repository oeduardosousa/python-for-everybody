# Complete Fitness Calculator

# Using functions to calculate Body Mass Index (BMI)
def calculate_bmi(weight, height):
    bmi = weight / (height ** 2)
    return bmi

# Get user input for weight and height
weight = float(input("Enter your weight in kilograms: "))
height = float(input("Enter your height in meters: "))

# Calculate BMI and display the result
bmi = calculate_bmi(weight, height)
print("Your BMI is:", bmi)

# Determine weight category based on BMI
if bmi < 18.5:
    print("You are underweight.")
elif 18.5 <= bmi < 24.9:
    print("You have a normal weight.")
elif 25 <= bmi < 29.9:
    print("You are overweight.")
else:
    print("You are obese.")
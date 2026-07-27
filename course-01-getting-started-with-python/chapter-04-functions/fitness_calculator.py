# Fitness Calculator

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
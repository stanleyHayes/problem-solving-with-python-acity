# Welcome user
print("Welcome to Olympus BMI Shop")
# Ask user of name
username = input("Enter your name:\t\t")  # username = Jasmine
# Ask for weight or mass
weight = float(input("Enter your weight in kg:\t"))  # weight = 50
# Ask for height
height = float(input("Enter your height in meters: \t"))  # height = 1.6
# Perform the calculation
bmi = weight / pow(height, 2)  # bmi = 19.531
# Output the result to user
print(f"Hello {username}, your body mass index is {bmi:010.5f} kg/m2")
print("Goodbye")

# escape sequences

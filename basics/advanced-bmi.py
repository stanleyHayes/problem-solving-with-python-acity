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
result = ''
if bmi >= 30:
    result = "obese"
elif 25 <= bmi:
    result = "overweight"
elif 18.5 <= bmi:
    result = "normal"
else:
    result = "underweight"

print(f"Hello {username}, your body mass index is {bmi:10.5f} kg/m2 hence you're {result}")
print("Goodbye")

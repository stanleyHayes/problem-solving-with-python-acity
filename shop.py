UNIT_MANGO = 1.5
# welcome the user to your program
print("Welcome to Olympus Shop")
# ask user for name
name = input("What is your name? ")
# ask the user the number of mangoes he or she is buying and take number from user ==> input
number_of_mangoes = int(input(f"Hello {name}, How many mangoes would you like to buy? "))
# calculate the total cost of the mangoes ==> processing
total_cost = number_of_mangoes * UNIT_MANGO
# display output to user ==> output
print(f'The total cost of {number_of_mangoes} mangoes is {total_cost} GHS')
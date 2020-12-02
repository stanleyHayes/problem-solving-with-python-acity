UNIT_ORANGE_PRICE = 1.0
UNIT_MANGO_PRICE = 1.5
UNIT_BANANA_PRICE = 1.8

UNIT_PRICE = 0
fruit = ""

print("Welcome to Advanced Olympus Shop")
print(
    f"Menu\n{'*' * 50}\n1 - Orange - {UNIT_ORANGE_PRICE} GHS\n2 - Banana - {UNIT_BANANA_PRICE} GHS\n3 - Mango - {UNIT_MANGO_PRICE} GHS")
user_choice = int(input("Select fruit to buy:\t"))
if user_choice == 1:
    UNIT_PRICE = UNIT_ORANGE_PRICE
    fruit = "Orange"
if user_choice == 2:
    UNIT_PRICE = UNIT_BANANA_PRICE
    fruit = "Banana"
if user_choice == 3:
    UNIT_PRICE = UNIT_MANGO_PRICE
    fruit = "Mango"
quantity = int(input(f"How many {fruit} do you want to buy: \t"))
total_cost = UNIT_PRICE * quantity
print(f"The total cost of {quantity} {fruit} with unit price {UNIT_PRICE} GHS is {total_cost} GH")

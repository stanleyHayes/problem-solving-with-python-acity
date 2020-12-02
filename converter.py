NAIRA_TO_CEDI = 64.91
# Welcome Person
print("Welcome to the Fuhrers Currency Converter: ")
# Ask user of name
name = input("Enter your name: \t\t\t")
# Ask for amount in GHS
amount_in_ghs = float(input("Enter amount in Ghana Cedis: "))
# Calculate amount in Naira
amount_in_naira = amount_in_ghs * NAIRA_TO_CEDI
# Output amount in naira to user
print(f"Hello {name}, {amount_in_ghs} GHS is equivalent to {amount_in_naira} naira.\n\n\n")
print("Goodbye")

# \n newline escape sequence
# \t horizontal tab

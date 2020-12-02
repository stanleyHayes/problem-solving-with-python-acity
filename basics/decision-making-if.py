# case 1
# 1 option
# execute or perform that action or do nothing
# if statement
# the condition is always an expression that evaluates to a boolean
# if condition evaluates (result after solving the expression) to False statement 1 ... statement n are not executed
# if condition evaluates to True statement 1 ... statement n are executed
"""
syntax
if condition :
    statement 1
    statement 2
    ...
    statement n
"""
PASS_MARK = 50  # define a variable called PASS_MARK and initialise it with a value of 50
# ask user to input mark
mark = float(input("Enter your mark:\t"))  # 78.0
if mark >= PASS_MARK:  # 78.0 >= 50 ===> True
    print(f'With a mark of {mark}, you have passed!!!')
    print("Congratulations")
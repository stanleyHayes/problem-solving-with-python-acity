# case 2
# two options or actions that we can choose from
# we can only choose one of the two actions
# there is one condition
# if the condition evaluates to True, True (if) block will be executed and the False block is skipped
# if the condition evaluates to False, False (else) block will be executed and the True block is skipped

"""
syntax
if condition :
    True Block
    statement 1
    statement 2
    ...
    statement n
else:
    False Block
    False statement a
    False statement b
    ...
    False statement q
"""
PASS_MARK = 50  # define a variable called PASS_MARK and initialise it with a value of 50
# ask user to input mark
mark = float(input("Enter your mark:\t"))  # 8.0
if mark >= PASS_MARK:  # 8.0 >= 50 ===> False
    print(f'With a mark of {mark}, you have passed!!!')
    print("Congratulations")
else:
    print(f'With a mark of {mark}, you have failed miserably')
    print("Wo gyimi you should have studied more")
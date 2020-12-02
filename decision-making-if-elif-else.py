# case 3
# multiple options to choose from
# choose a maximum of one option
# more than one condition
# one option per condition
# if condition1 is evaluates to True, only Condition 1 Block is executed
# if condition1 evaluates to False, condition2 is checked
# if condition2 evaluates to True, only Condition 2 Block is executed
# if condition2 evaluates to False, ... the pattern continues
# if none of the conditions evaluates to True, the else Block is executed
# the Else block is optional. if present and none of the conditions above it
# evaluates to True, it will be executed
# if the Else block is not present, and none of the conditions evaluates to True,
# nothing no block will be evaluated
"""
syntax
if condition1 :
   Condition 1 Block
   statement 1
   statement 2
   ...
   statement n
elif condition2 :
    Condition 2 Block
    statement a
    statement b
    ...
    statement q
...
else:
    Else Block
    statement I
    statement II
    ...
    statement LLL
"""

# Grading System
# 75 - 100 ===> A
# 70 - 74 ===> B2
# 69 - 65 ===> B3
# 64 - 60 ===> C4
# 59 - 55 ===> C5
# 54 - 50 ===> C6
# 49 - 45 ===> D7
# 44 - 40 ===> E8
# 30 - 0 ====> F9

# ask name from user
name = input("Enter name: ")
# ask course from user
course = input("Enter course: ")
# ask mark from user
mark = float(input(f"Enter mark for {course}: "))

grade = ''
if 75 <= mark <= 100:
    grade = 'A'
elif 70 <= mark:
    grade = 'B2'
elif 65 <= mark:
    grade = 'B3'
elif 60 <= mark:
    grade = 'C4'
elif 55 <= mark:
    grade = 'C5'
elif 50 <= mark:
    grade = 'C6'
elif 45 <= mark:
    grade = 'D7'
elif 40 <= mark:
    grade = 'E8'
elif 0 <= mark:
    grade = 'F9'
else:
    grade = 'ungraded'
print(f'Hello {name}, you obtained a grade of {grade} in the course {course}')

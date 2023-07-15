"""
Python Principles Challenge
-----------------------------------------------------------------------------------------------
Challenge:
Type Check
Write a function named only_ints that takes two parameters.
Your function should return True if both parameters are integers, and False otherwise.

For example, calling only_ints(1, 2) should return True,
while calling only_ints("a", 1) should return False.
-----------------------------------------------------------------------------------------------
Challenge Start Date:   2023-07-15
Challenge End Date:     2023-07-15
"""
def only_ints(par1, par2):
    if type(par1) == int and type(par2) == int:
        return True
    else:
        return False


number1 = 1
number2 = 2
result = only_ints(number1, number2)
print(result)

number1 = 1
number2 = "a"
result = only_ints(number1, number2)
print(result)

number1 = 1
number2 = True
result = only_ints(number1, number2)
print(result)

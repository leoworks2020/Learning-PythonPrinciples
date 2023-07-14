"""
Python Principles Challenge
-----------------------------------------------------------------------------------------------
Challenge:
Randomness
Define a function, random_number, that takes no parameters.
The function must generate a random integer between 1 and 100, both inclusive, and return it.

Calling the function multiple times should (usually) return different numbers.

For example, calling random_number() some times might first return 42, then 63, then 1.
-----------------------------------------------------------------------------------------------
Challenge Start Date:   2023-07-14
Challenge End Date:
"""
import random

def random_number():
    result = random.randrange(1,100+1)
    return result

n = random_number()
print(n)

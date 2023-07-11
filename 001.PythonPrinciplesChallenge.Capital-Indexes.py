"""
Python Principles Challenge
-----------------------------------------------------------------------------------------------
Challenge:
Capital indexes
Write a function named capital_indexes.
The function takes a single parameter, which is a string.
Your function should return a list of all the indexes in the string that have capital letters.

For example, calling capital_indexes("HeLlO") should return the list [0, 2, 4].
-----------------------------------------------------------------------------------------------
Challenge Start Date: 2023-07-10
Challenge End Date: 2023-07-10
"""

def capital_indexes(string):
    capital_letters = list
    indexes = list
    position = int
    capital_letters = []
    indexes = []
    position = 0
    for w in string:
        if position == len(string):
            break
        if w == w.upper():
            #capital_letters.append(w)
            #indexes.append(string.index(w))
            indexes.append(position)
        position += 1
    return indexes

indexes = capital_indexes("HeLlO")
print(indexes)
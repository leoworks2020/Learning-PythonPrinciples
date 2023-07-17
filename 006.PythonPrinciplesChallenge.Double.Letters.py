"""
Python Principles Challenge
-----------------------------------------------------------------------------------------------
Challenge:
Double Letters
The goal of this challenge is to analyze a string to check if it contains two of the same letter in a row.
For example, the string "hello" has l twice in a row, while the string "nono" does not have two identical letters in a row.

Define a function named double_letters that takes a single parameter.
The parameter is a string.
Your function must return True if there are two identical letters in a row in the string, and False otherwise.
-----------------------------------------------------------------------------------------------
Challenge Start Date:   2023-07-17
Challenge End Date:     2023-07-17
"""
def double_letters(word):
    previous_word = ""
    for w in word:
        if w == previous_word:
            return True
        previous_word = w
    return False

result = double_letters("Hello")
print(result)
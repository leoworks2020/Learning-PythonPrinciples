"""
Python Principles Challenge
-----------------------------------------------------------------------------------------------
Challenge:
Adding and Removing Dots
Write a function named add_dots that takes a string and adds "." in between each letter.
For example, calling add_dots("test") should return the string "t.e.s.t".

Then, below the add_dots function, write another function named remove_dots that removes all dots from a string.
For example, calling remove_dots("t.e.s.t") should return "test".

If both functions are correct, calling remove_dots(add_dots(string))
should return back the original string for any string.

(You may assume that the input to add_dots does not itself contain any dots.)
-----------------------------------------------------------------------------------------------
Challenge Start Date:   2023-07-19
Challenge End Date:     2023-07-19
"""
def add_dots(string):
    dots_string = ""
    for w in range(len(string)):
        dots_string = dots_string + string[w] + "."
    dots_string = dots_string.strip(".")
    return dots_string

def remove_dots(string):
    no_dots_string = string.replace(".","")
    return no_dots_string


string = input()
result1 = add_dots(string)
print(result1)

result2 = remove_dots(result1)
print(result2)

result3 = remove_dots(add_dots(result1))
print(result3)
"""
Python Principles Challenge
-----------------------------------------------------------------------------------------------
Challenge:
Counting Syllables
Define a function named count that takes a single parameter.
The parameter is a string.
The string will contain a single word divided into syllables by hyphens, such as these:

"ho-tel"
"cat"
"met-a-phor"
"ter-min-a-tor"

Your function should count the number of syllables and return it.

For example, the call count("ho-tel") should return 2.
-----------------------------------------------------------------------------------------------
Challenge Start Date:   2023-07-20
Challenge End Date:     2023-07-20
"""
def count(word):
    word_list = word.split("-")
    count = len(word_list)
    return count

print("Please input a hyphanized word:")
input_word = input()
result = count(input_word)
print(result)
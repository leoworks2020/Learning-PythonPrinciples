"""
Python Principles Challenge
-----------------------------------------------------------------------------------------------
Challenge:
Anagrams
Two strings are anagrams if you can make one from the other by rearranging the letters.

Write a function named is_anagram that takes two strings as its parameters.
Your function should return True if the strings are anagrams, and False otherwise.

For example, the call is_anagram("typhoon", "opython")
should return True while the call is_anagram("Alice", "Bob") should return False.
-----------------------------------------------------------------------------------------------
Challenge Start Date:   2023-08-03
Challenge End Date:     2023-08-03
"""
def is_anagram(w1, w2):
    w1list = []
    w2list = []
    w1list = [ letters for letters in w1 ]
    w2list = [letters for letters in w2]
    w1list.sort()
    w2list.sort()
    if w1list == w2list:
        return True
    else:
        return False

w1 = "typhoon"
w2 = "opython"
result = is_anagram(w1, w2)
print(result)

w1 = "Alice"
w2 = "Bob"
result = is_anagram(w1, w2)
print(result)

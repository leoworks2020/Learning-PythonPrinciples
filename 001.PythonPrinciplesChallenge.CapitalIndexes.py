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
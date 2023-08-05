dictionaryOne = {"Janet": 87, "Logan": 62, "Whitaker": 46, "Alyssa": 100, "Stef": 80, "Jeff": 88, "Kim": 52, "Sylvia": 95}
dictionaryTwo = {"Logan": 62,"Kim": 52, "Whitaker": 52, "Jeff": 88, "Stef": 80, "Brian": 60, "Lisa": 83, "Sylvia":87}

def intersect(dictionaryOne,dictionaryTwo):
    newDictionary = {}
    for key in dictionaryOne:
        if key in dictionaryTwo and dictionaryOne[key] == dictionaryTwo[key]:
            newDictionary[key] = dictionaryOne[key]
    return newDictionary
print(intersect(dictionaryOne,dictionaryTwo))

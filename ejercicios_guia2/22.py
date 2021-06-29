i = input()
iList = [str(x) for x in i]

for x in iList:
    if x == "a" or x == "A":
        iList[iList.index(x)] = "X"
    elif x == "e" or x == "E":
        iList[iList.index(x)] = "X"
    elif x == "i" or x == "I":
        iList[iList.index(x)] = "X"
    elif x == "o" or x == "O":
        iList[iList.index(x)] = "X"
    elif x == "u" or x == "U":
        iList[iList.index(x)] = "X"

i = "".join(iList)

print(i)
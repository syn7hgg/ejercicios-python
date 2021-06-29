i = input()
iList = [str(x) for x in i]

print(iList)

for x in iList:
    if x == "a" or x == "A":
        iList[iList.index(x)] = "1"
    elif x == "e" or x == "E":
        iList[iList.index(x)] = "2"
    elif x == "i" or x == "I":
        iList[iList.index(x)] = "3"
    elif x == "o" or x == "O":
        iList[iList.index(x)] = "4"
    elif x == "u" or x == "U":
        iList[iList.index(x)] = "0"

i = "".join(iList)

print(i)
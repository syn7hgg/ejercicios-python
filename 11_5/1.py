# Ahorcado (UNFINISHED)
from random import choice

# uVars
attCount, hitCount, missCount, missList, hitList = 0, 0, 0, [], []
# cVars
debug = True


def verify_attempt(att_str):
    global attCount, hitCount, hitList, missList
    if att_str in selWord:
        hitCount += 1
        hitList.append(attStr)
    else:
        missList.append(attStr)
    attCount += 1


def verify_word():
    global hitList, missList, selWord, missCount
    for x in hitList:
        if str(x) not in selWord:
            missCount += 1
    if missCount == 0 and len(hitList) == len(selWord):
        print("Has ganado.")


def render():
    global attCount, hitCount
    missCount = attCount - hitCount
    printed = 0
    print("   + - - - +")
    print("   |       |")
    if missCount > 0:
        print("   O       |")
        printed += 1
    else:
        print("           |")
        printed += 1
    if missCount > 1:
        if missCount == 2:
            print("   |       |")
            printed += 1
        elif missCount == 3:
            print("  /|       |")
            printed += 1
        elif missCount > 3:
            print("  /|\      |")
            printed += 1
        else:
            print("           |")
            printed += 1
    if missCount > 4:
        if missCount == 5:
            print("  /        |")
            printed += 1
        if missCount > 5:
            print("  / \      |")
            printed += 1
        else:
            print("           |")
            printed += 1
    while printed < 4:
        print("           |")
        printed += 1
    print("==============")


def print_info():
    global missList, hitList, selWord
    missStr = " ".join(missList)
    print("Letras incorrectas:", missStr)
    hitStr = " ".join(hitList)
    print("Letras correctas:", hitStr)
    for x in selWord:
        for y in hitList:
            if y in selWord:
                print("", y, " ")
                break


wordList = 'hormiga babuino tejon murcielago oso castor camello gato almeja cobra pantera ' \
           'coyote cuervo ciervo perro burro pato aguila huron zorro rana cabra ganso halcon ' \
           'leon lagarto llama topo mono alce raton mula salamandra nutria buho panda loro ' \
           'paloma piton conejo carnero rata cuervo rinoceronte salmon foca tiburon oveja ' \
           'mofeta perezoso serpiente araña cigüeña cisne tigre sapo trucha pavo tortuga comadreja ' \
           'ballena lobo wombat cebra'.split()

selWord = choice(wordList)
if debug:
    print(selWord)
while len(missList) < 6:
    attStr = input("Ingrese una letra: ").lower()
    verify_attempt(attStr)
    render()
    print_info()

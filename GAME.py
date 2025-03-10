import random

while True:
    try:
        lvl = int(input("Level: "))
        if lvl > 0:
            break
    except:
        pass
ranum = random.randint(1, lvl)

while True:
    try:
        q = int(input("Guess: "))
        if q > 0:
            if ranum > q: print("Too small!")
            elif ranum < q: print("Too large!")
            else:
                print("Just right!")
                break

    except:
        pass


import random


def main():
    lvl = get_level()
    score = thegame(lvl)
    print("Score:", score)

def get_level():
    while True:
        try:
            lvl = int(input("Level: "))
            if lvl in [1,2,3]:
                break
        except:
            pass
    return lvl

def mathround(x, y):
    roundcount = 1
    while roundcount <= 3:
        ans = int(input(f'{x} + {y} = '))
        if ans == (x + y):
            return True
        else:
            roundcount += 1
            print("EEE")
    print(f"{x} + {y} == {x + y}")
    return False

def thegame(lvl):
    count = 1
    score = 0
    while count <=10:
        x, y = generate_integer(lvl)
        res = mathround(x, y)
        if res == True:
            score += 1
        count += 1
    return score


def generate_integer(lvl):
    if lvl == 1:
        x = random.randint(0, 9)
        y = random.randint(0, 9)
    elif lvl == 2:
        x = random.randint(10, 99)
        y = random.randint(10, 99)
    else:
        x = random.randint(100, 999)
        y = random.randint(100, 999)
    return x, y
if __name__ == "__main__":
    main()

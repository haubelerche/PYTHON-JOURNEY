while True:
    try:
        prompt = input("Fraction:")
        x, y = prompt.split("/")
        newx = int(x)
        newy = int(y)
        m = round(newx/newy * 100)
        if m <= 1:
            print("E")
            break
        elif newx > newy or newy == 0:
            pass
        elif m >= 99:
            print("F")
            break
        else:
            print(f"{m}%")
            break
    except (ValueError, ZeroDivisionError):
        pass





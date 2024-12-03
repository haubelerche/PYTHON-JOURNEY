for i in range(int(input())):
    def checkso(x):
        if len(x) <3: return 'NO'
        i = 0
        while i < len(x) - 1 and x[i] < x[i+1]: i += 1
        while i < len(x) - 1 and x[i] > x[i+1]: i += 1
        if i == len(x) - 1: return 'YES'
        return 'NO'
    print(checkso((input())))
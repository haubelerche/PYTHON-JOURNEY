def checkstring():
    s=input()
    res = "YES"
    for i in s:
        if i!='4' and i!='7': res = "NO"
    print(res)


if __name__ =='__main__':
    for i in range(int(input())):
        checkstring()
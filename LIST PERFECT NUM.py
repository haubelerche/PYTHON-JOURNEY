a =[]
def check(n):
    for i in n:
        if int(i) % 2 ==1:
            return False
        return True     
num = 2
while num <= 888:
    if check(str(num)):
        x = str(num)
        a.append(int(x + x[::-1]))
    num += 2

if __name__ =="__main__":
    t =int(input())
    while t > 0:
        n = int(input())
        for i in a:
            if i >= n:
                break
            print(i, end = " ")
        print()
        t -= 1
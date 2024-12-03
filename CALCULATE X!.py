#tính s=1!!-2!!+3!!-4!!+...+(-1)^k+1k!!(với k < 1000)
def fac2(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n *fac2(n -2)
if __name__ =="__main__":
    k = int(input("nhap k: "))
    tong = 0
    for i in range(1, k+1):
        tong += fac2(i)*((-1)**(i+1))
        print(tong)
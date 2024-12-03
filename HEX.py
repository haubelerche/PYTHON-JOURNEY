def he2(n):
    if n < 2:
        print(n, end = "")
        return
    he2(n//2)
    print(n % 2, end = "")
def he16(n):
    if n != 0:
        he16(n//16)
        r = n % 16
        if r < 10:
            print(r, end = "")
        else:
            print(chr(r+55), end = "")

if __name__ == "__main__":
    he2(10)
    print()
    he16(10)
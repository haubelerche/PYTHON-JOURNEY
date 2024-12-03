x, pheptinh, y = input().split()

x = float(x)
y = float(y)

ketqua = None

if pheptinh == "+":
    ketqua = x + y
elif pheptinh == "-":
    ketqua = x - y
elif pheptinh == "*":
    ketqua = x * y 
elif pheptinh == ":" or pheptinh == "/":
    if y == 0:
        print("Y phai khac 0")
    else:
        ketqua = x/y

if ketqua != None:
    print("{} {} {} = {}".format(x, pheptinh, y, ketqua))
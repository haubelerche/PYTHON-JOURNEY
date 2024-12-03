print("Vui lòng nhập vào ba cạnh của tam giác cách nhau bởi khoảng trắng:")
try:
    a, b, c = map(float, input().split())
    if a <= 0 or b <= 0 or c <= 0:
        print("Các cạnh phải lớn hơn 0!")
    elif a + b > c and a + c > b and b + c > a:
        print("{},{},{} là ba cạnh của một tam giác". format(a, b, c))
    else:
        print("{},{},{} không là ba cạnh của một tam giác". format(a, b, c))
except:
   print("Định dạng đầu vào không hợp lệ!")
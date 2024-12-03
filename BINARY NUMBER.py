from random import randint
while True:
    np = ''.join(str(randint(0, 1)) for _ in range(randint(1, 10)))
    print(f"Số nhị phân ngẫu nhiên: {np}")
    break

thaphan = int(np, 2)

while True:
    hoi = int(input('Nhập lựa chọn của bạn (1, 2 hoặc 3): '))
    if hoi == 1:
        with open("cs1.txt", "a", encoding='utf-8') as file:
            file.write(f"Số nhị phân: {np}, Số thập phân: {thaphan}\n")
        print(f"Số nhị phân {np} tương đương với số thập phân {thaphan}")

    if hoi == 2:
        sohex = hex(thaphan)[2:].upper()
        with open("cs2.txt", "a", encoding='utf-8') as file1:
            file1.write(f"Số nhị phân: {np}, Số thập lục phân: {sohex}\n")
        print(f"Số nhị phân {np} tương đương với số thập lục phân {sohex}")
    elif hoi == 3:
        print("Kết thúc chương trình.")
        break

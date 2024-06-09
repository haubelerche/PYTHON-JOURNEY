"""
Xây dựng chương trình quản lý tiêu thụ điện của 1 chung cư như sau:
Nhập thông tin các hộ sử dụng điện, biết mỗi hộ cần nhập các thông tin: 
Số phòng, Mã tòa nhà, Tên chủ hộ, Số Kwh tiêu thụ. 
Các thông tin nhập cần thỏa mãn điều kiện: Số phòng, Mã tòa nhà và Tên chủ hộ phải khác rỗng, Số Kw tiêu thụ phải >=0. 
Nếu người dùng nhập không đúng, thì chương trình yêu cầu nhập lại cho đến khi thỏa mãn điều kiện.

Xây dựng hàm tính tiền điện, như sau:
* 100 Kw đầu: giá 1450 đồng/Kw
• Từ 101 đến 150 Kw: giá 1750 đồng/Kw
• Từ 151 trở lên: giá 2000 đồng/Kw
• Thuế VAT bằng 10% tổng tiền phải trả
Hiển thị tất cả các hộ đang sử dụng điện theo định dạng:
Số phòng|Mã tòa nhà |Tên chủ hộ|Số Kwh|Tổng tiền|105|CT2|Nguyễn Văn An 10|14500

Ghi nối tiếp các thông tin vừa nhập vào cuối tệp văn bản có tên là dsdien.txt
"""

def checkdk(sophg, manha, tenchu, kwh):
    if sophg and manha and tenchu != "" or kwh >= 0:
        return True
    else:
        return False


def tinh_phi(kwh):
    if kwh <= 100:
        chphi = kwh * 1450
    elif 100 < kwh <= 150:
        chphi = 100 * 1450 + ( kwh - 100) * 1750
    else:
        chphi = 100 * 1450 + 50 * 1750 + ( kwh - 150) * 2000
    tongtien = round(chphi * 1.1)
    return tongtien

#mo file
file = open('dsdien.txt', 'a', encoding='utf-8')
while True:
    sophg = input("Nhập số phòng: ")
    if sophg == "":
        break
    manha = input("Nhập mã tòa nhà: ")
    tenchu = input("Nhập tên chủ hộ: ")
    kwh = float(input("Nhập số Kwh điện sử dụng: "))
    if checkdk(sophg, manha, tenchu, kwh):
        tongtien = tinh_phi(kwh)
        file.write('\t'.join([sophg, manha, tenchu, str(kwh), str(tongtien)]) + '\n')
        chay = input("Bạn muốn tiếp tục nhập thông tin? (Y/N): ")
        if chay.lower() == "n":
            break
file.close()

print("Danh sách tiền điện các hộ gia đình: ")
print('\t'.join(["Số phòng", "Mã tòa nhà", "Tên chủ hộ", "Số Kwh", "Tổng tiền"]))
file = open('dsdien.txt', 'r', encoding='utf-8')
for sophg in file.readlines():
    print(sophg.replace("\n",""))
file.close()

    

from datetime import datetime
import pandas as pd


def tuoi(ns):
    return datetime.today().year - ns


def luong(sn):
    if int(sn) >= 25:
        return int(200000*sn)
    elif int(sn) < 15:
        return int(150000*sn)


def ghichu(sn):
    if int(sn) >= 25:
        return 'Chăm chỉ'
    elif int(sn) < 15:
        return 'Nghỉ nhiều'


with open('congnhan.csv', 'a', encoding='utf-8') as file:
    while True:
        mcn = input('Nhập mã công nhân: ')
        if mcn.strip() == '':
            print('Vui long nhap lai!')
            continue

        tcn = input('Nhap ten cong nhan: ')
        if tcn.strip() == '':
            print('Vui long nhap lai!')
            continue

        ns = int(input("Nhập năm sinh: "))
        if ns <= 1960 or ns >= 2001:
            print("Năm sinh không được nhỏ hơn 1900, vui lòng nhập lại.")
            continue

        sn = int(input('Nhap so ngay lam viec trong thang: '))
        if sn >= 31:
            print('Vui long nhap lai!')
            continue

        cf = input("Tiếp tục nhap? (Y/N)")
        if cf == 'N' or cf == 'n':
            break
    file.write('\t'.join([mcn, tcn, str(ns), str(sn)]) + '\n')

res = True
while res:
    hoi = int(input("Nhap vao lua chon cua ban (1, 2 hoac 3): "))
    if hoi == 1:
        df = pd.DataFrame(columns=['Mã công nhân', 'Tên công nhân','Năm sinh', 'Số ngày làm trong tháng', 'Tuổi công nhân'])
        df = df._append({
            'Mã công nhân': mcn,
            'Tên công nhân': tcn,
            'Năm sinh': ns,
            'Số ngày làm trong tháng': sn,
            'Tuổi công nhân': tuoi(ns)}, ignore_index=True)
        df.to_csv('congnhan.csv', sep='\t', index=False)
        print(df)
    if hoi == 2:
        df = pd.DataFrame(columns=['Mã công nhân', 'Tên công nhân', 'Năm sinh', 'Số ngày làm trong tháng', 'Tuổi công nhân', 'Lương', 'Ghi chú'])
        df = df._append({
            'Mã công nhân': mcn,
            'Tên công nhân': tcn,
            'Năm sinh': ns,
            'Số ngày làm trong tháng': sn,
            'Tuổi công nhân': tuoi(ns),
            'Lương': luong(sn),
            'Ghi chú': ghichu(sn)}, ignore_index=True)
        df.to_csv('congnhan.csv', sep='\t', index=False)
        print(df)
    if hoi == 3:
        break
from datetime import datetime
import pandas as pd
import numpy as np
with open('dshs.txt', 'a', encoding='utf-8') as df1:
    while True:
        hoten = input("Nhập tên học sinh: ")
        if hoten.strip() == "":
            print("Họ và tên không được để trống, vui lòng nhập lại.")
            continue

        namsinh = int(input("Nhập năm sinh của học sinh: "))
        if namsinh == '':
            print("Năm sinh không được để trống hoặc chứa kí tự chữ cái, vui lòng nhập lại.")
            continue

        tenph = input("Nhập tên phụ huynh học sinh: ")
        if tenph.strip() == '':
            print("Tên phụ huynh không được để trống, vui lòng nhập lại.")
            continue
        ns = int(input("Nhập năm sinh: "))
        if ns <= 1900:
            print("Năm sinh không được nhỏ hơn 1900, vui lòng nhập lại.")
            continue

        sdt = int(input("Nhập số dien thoại liên hệ: "))
        if sdt == '':
            print("Số điện thoại liên hệ không được để trống hoặc chứa chữ cái, vui lòng nhập lại.")
            continue

        cf = input("Tiếp tục nhap? (Y/N)")
        if cf == 'N' or cf == 'n':
            break
    df1.write('\t'.join([hoten, str(namsinh), tenph, str(ns), str(sdt)]) + '\n')
res = True
while res:
    hoi = int(input("Nhap vao lua chon cua ban (1, 2 hoac 3): "))
    if hoi == 1:
        df = pd.read_csv('dshs.txt', sep='\t', names=['Họ và tên', 'Năm sinh', 'Họ và tên P.H', 'Năm sinh P.H', 'SĐT'])
        cyear = datetime.today().year
        df['Tuổi học sinh'] = cyear - df['Năm sinh']
        print(df, sep='\t')
        df.to_csv('Hocsinh.txt', sep='\t', index=False)
    if hoi == 2:
        df2 = pd.read_csv('Hocsinh.txt', sep='\t')
        df2['Lớp'] = np.where(df2['Tuổi học sinh'] == 1, 'Mầm',
                             np.where(df2['Tuổi học sinh'] == 2, 'Chồi',
                                     np.where(df2['Tuổi học sinh'] == 3, 'Lá', 'Nhà trẻ')))
        print(df2, sep='\t')
        df2.to_csv('Hocsinh.txt', sep='\t', index=False, header=False)

    if hoi == 3:
        print('Ket thuc')
        break
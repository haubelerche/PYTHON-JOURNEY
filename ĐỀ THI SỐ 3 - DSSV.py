#cre: Hậu Lương hehehe
import pandas as pd
with open('dschug.txt', 'a', encoding='utf-8') as df0:
    while True:
        hoten = input("Nhập họ và tên: ")
        if hoten.strip() == "":
            print("Họ và tên không được để trống, vui lòng nhập lại.")
            continue
        msv = input("Nhập mã sinh viên: ")
        if msv.strip() == "":
            print("Mã sinh viên không được để trống, vui lòng nhập lại.")
            continue
        dtl = float(input("Nhập điểm tích lũy: "))
        if dtl <= 0:
            print("Điểm tích lũy không được nhỏ hơn 1, vui lòng nhập lại.")
            continue
        tccd = int(input("Nhập số tín chỉ chưa đạt: "))
        cf = input("Tiếp tục nhap? (Y/N)")
        if cf == 'N' or cf == 'n':
            break
    df0.write('\t'.join([hoten, msv, str(dtl), str(tccd)]) + '\n')
res = True
while res:
    hoi = int(input('Nhập lựa chọn của bạn (1 hoặc 2 hoặc 3): '))
    if hoi == 1:
        df = pd.read_csv('dschug.txt', sep='\t', names=['Họ và tên', 'Mã sinh viên', 'Điểm tích lũy', 'Số tín chỉ chưa đạt'])
        print('\nDanh sách sinh viên đủ điều kiện làm khóa luận\n')
        locsv = df[(df['Điểm tích lũy'] >= 2.8) & (df['Số tín chỉ chưa đạt'] <= 5)]
        print(locsv)
        locsv.to_csv('dskl.txt', sep='\t', index=False)
    if hoi == 2:
        df1 = pd.read_csv('dschug.txt', sep='\t', names=['Họ và tên', 'Mã sinh viên', 'Điểm tích lũy', 'Số tín chỉ chưa đạt'])
        df1['Xếp loại'] = df1.apply(lambda row: 'Xuất sắc' if row['Điểm tích lũy'] >= 3.5 else 'Giỏi' if row['Điểm tích lũy'] >= 3.2 else 'Khá' if row['Điểm tích lũy'] >= 2.5 else 'Trung bình', axis=1)
        df1.to_csv('xlsv.txt', sep='\t', index=False)
        print('\nDanh sách xếp loại sinh viên\n')
        print(df1)
    if hoi == 3:
        print('Hết rồi nhìn gì :)')
        break
  



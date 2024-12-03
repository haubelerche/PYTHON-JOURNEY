# -*- coding: utf-8 -*-
"""
Created on Tue Apr  2 21:47:33 2024

@author: admin
"""
ds = {
"tên": "Máy tính bảng", "nhà sản xuất": "Apple", "giá": 800,
"tên": "Điện thoại", "nhà sản xuất": "Samsung", "giá": 1000,
"tên": "Điều hòa", "nhà sản xuất":"Panasonic", "giá": 1200
}
#Tạo ds các mặt hàng của nsx "Samsung"
kq = {}

for i in ds:
    if i{"Nhà sản xuất"} = {"Samsung"}:
    kq.append(i)
#Hiển thị danh sách các mặt hàng của nsx "Samsung"
for j in kq:
    print(j)
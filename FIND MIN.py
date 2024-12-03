t = int(input())
for i in range(t) :
    n = input()
    n = n + 'z'
    ans = 10 * 20
    s = 0
    for i in range(len(n)) :
        if n[i].isalpha() :
            if i != 0 and n[i - 1].isdigit() : ans = min(ans, s)
            s = 0
        else : s = s * 10 + int(n[i])
    print(ans)

#chạy bộ test, sau đó nhập chuỗi n. xét chuỗi n ko thiếu character nào cho tới z.
#theo đề bài thì số nhỏ hơn 10^20 nên thêm variable ans để tạo limit độ lớn của số.
#tạo số nhỏ nhất s, gán tạm là 0
#tạo vòng lặp theo độ dài của chuỗi n nhập vào. 
#truy các giá trj chữ: nếu giá trị là số thì ans = 


# Sau đó, với mỗi bộ test, chương trình sẽ đọc xâu ký tự và thêm ký tự 'z' vào cuối xâu để đảm bảo rằng số cuối cùng cũng được xử lý.
#Chương trình sẽ duyệt qua từng ký tự trong xâu và tính toán số nhỏ nhất. Khi gặp ký tự chữ, chương trình sẽ kiểm tra xem ký tự trước đó có phải là số hay không. 
#Nếu có, chương trình sẽ cập nhật kết quả là số nhỏ nhất cho đến thời điểm đó. 
#Sau đó, chương trình sẽ reset giá trị s về 0 để tính toán số tiếp theo.
#Cuối cùng, chương trình sẽ in ra kết quả của mỗi bộ test.









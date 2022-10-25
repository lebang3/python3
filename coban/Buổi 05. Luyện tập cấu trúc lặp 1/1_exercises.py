"""
for i in range(2, n+1): -> kiem tra tung so trong khoang 2, n
    count = 0 -> dem so uoc
    ...
    if count
        ...
    else
        ...

-> Đếm snt từ 2 -> n
    -> xét lặp từ 2-> n, số của lần lặp hiện tại là i 
    -> kiểm tra i có phải snt hay không
    -> Đưa ra kết luận

-> i sẽ có vai trò như là n trong bài trước (là số cần kiểm tra xem có phải snt không)
"""

a = int(input('Nhap vao so a: '))
b = int(input('Nhap vao so b: '))

for i in range(a, b+1):
    count = 0 
    for j in range(1, i + 1):
        if i % j == 0:
            count = count + 1
    if count > 2:
        print(i, "khong phai la so nguyen to")
    else:
        print(i, "la so nguyen to")
"""
Packing
-> khai báo tuple không cần dấu ()
"""

a = 1, 2, 'a', [1, 2, 'mnk']
print(a, type(a), a[2])

"""
Unpacking là:
- lấy giá trị từ bên trong tuple
- Gán lại vào các biến
============
- số biến = số phần tử trong tuple
- số biến < số phần tử
"""
### số biến = số phần tử
m1, m2, m3, m4 = a
print(m1, type(m1))
print(m4, type(m4))

### số biến < số phần tử
m1, *m2 = a
print(m1, m2, type(m1), type(m2))

*m1, m2 = a
print(m1, m2, type(m1), type(m2))

m1, *m3, m2 = a
print(m1, m2, type(m1), type(m2), m3, type(m3))

"""
Thử nghiệm - Đánh giá - Giải thích
Có khả năng xuất hiện 2 dấu * trong phép unpacking không. tại sao?

Không thể -> nhập nhằng vị trí phân biệt 2 bên
"""

"""
Trong Python có phép khai báo nhiều biến trong cùng một dòng. Ví dụ:
a, b, c = 1, 2, 3
Đây có thực sự là phép khai báo biến không? Bản chất là gì?
"""

a, b, c = 1, 2, 3

print(type((1, 2, 3)))
## vế trái: unpacking tuple
## vế phải: packing tuple
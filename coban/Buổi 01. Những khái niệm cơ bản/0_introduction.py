"""
0. Những khái niệm cơ bản
-----
- Máy tính không hiểu khái niệm đặc biệt
- nó chỉ hiểu được các con số - dữ liệu - câu lệnh
"""

print('Hello world!')

"""
1. Biến kiểu dữ liệu:
>>> 1
1
>>> 0.2
0.2
>>> 'Hello World!'
'Hello World!'
>>> a = 10

-> có 3 kiểu giá trị của dữ liệu chính: int, float, str
-> kiểm tra kiểu dữ liệu -> type(5)

-> Tại sao 1.2 - 1.0 lại ra 0.19999

[VN] Biểu diễn số thực trong máy tính - tại sao biểu diễn số thực lại không chính xác

type(1)
"""

"""
2. Biến

Biến là nơi để lưu trữ - truy cập - tương tác với giá trị trong nó

Biến có một định danh - gọi là tên biến. 
Tên biến sẽ 
"""

x = 10
print('x:', x)
x = 20
print('x:', x)

x = 'a'
x = 10.2
x = 10.2 + 5

print(x)

"""
Bài tập
-------
Khai báo biến y = 10
print(y, type(y), y + 5)
khai báo z = y + 2.5
print(z, type(z))
"""

y = 10
print(y, type(y), y + 10)
z = y + 2.5
print(z, type(z))


a = 10
a = a + 2
# b = a + 5
# b = b + 2

"""
Sau đoạn lệnh 65 -68. Giá trị của b là bao nhiêu? Tại sao?

-> Phép gán - 0 phải là dấu = toán học
-> thứ tự thực hiện
    - vế phải
        - thay 10 vào a
        -> a = 10 + 2
        -> a = 12
"""

"""
Đặt tên biến:
- Sử dụng kiểu snake case
-> các từ cách nhau bởi dấu _
"""

"""
Tóm tắt:
1. Giá trị là gì? Có nhiêu kiểu dữ liệu cơ bản thường gặp nào của giá trị?

2. Biến là gì? Cách gán giá trị cho biến? Đặt tên biến thế nào cho đúng chuẩn
"""
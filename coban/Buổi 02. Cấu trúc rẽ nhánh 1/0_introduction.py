"""
- Biểu thức logic
- Cấu trúc rẽ nhánh 1
"""

"""
1. Kiểu dữ liệu - toán tử - biểu thức boolean
- Hỗ trợ kiểu dữ liệu Boolean
    - True
    - False


Bài tập ôn tập:
1. Nhập vào python prompt giá trị True - False. Kiểm tra kiểu dữ liệu
của nó
2. Khai báo biến a, b giá trị boolean. Kiểm tra kiểu dữ liệu, id của biến
a, b
"""

print(type(True), id(True))
print(type(False), id(False))

"""
1.1 Toán tử so sánh
>>> 5 > 2
True
>>> 'a' > 'Z'
True
>>> 'a' < 'z'
True
>>> 2.5 <= -1
False
- nếu dùng input -> dùng kiểu str
nếu nhập 9.25 , 20.5
nó sẽ kết luận '9.25' > '20.5'
-> phải dùng kiểu float
"""

a = float(input("Nhập số a: "))
b = float(input("Nhập số b: "))
print(a > b, type(a > b))
print(a < b, type(a < b))
print(a == b, type(a == b))
print(a != b, type(a != b))

"""
Bài tập 1 + 2
"""

x = float(input("Nhập số x:\n"))
print(x > 0, type(x > 0 ))
print(x < 0, type(x < 0))
print(x < 0, type(x == 0))

x = int(input("Nhập lại số x:\n"))
print('x là số chẵn?:', x % 2 == 0)
print('x là số lẻ?:', x % 2 != 0) # x % 2 == 1

x = float(input("Nhập số x:\n"))
y = float(input("Nhập số y:\n"))
print(5 > 2 and (3 + 2) < 4)
print(2 > -1 or (x + 1) > y)
print(x >= 5 and (x <= 11)) # x có thuộc đoạn [5 , 11] không
print(x < 5 or (x > 11)) # kiểm tra x có ngoài khoảng (5, 11) không
print(x != 0 and (y / x) > 3)
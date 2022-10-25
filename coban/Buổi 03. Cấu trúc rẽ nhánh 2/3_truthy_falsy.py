"""
Chuyển đổi kiểu dữ liệu về bool (True/False)
-> Sử dụng hàm bool()
>>> bool(0)
False
>>> bool(-1)
True
>>> bool(1)
True
>>> bool('')
False
>>> bool('a')
True
>>> bool(0.0)
False
>>> bool(0.1)
True
"""

if 0:
    print('0 là True')
else: # Vào khối lệnh này
    print('0 là False')

if not '': # Vào khối lệnh này
    print('"" là False')
else:
    print('"" là True')

x = int(input('Nhập vào 1 số: '))
# Trước
# if x % 2 == 0:
#     print(x, 'là số chẵn')
# else:
#     print(x, 'là số lẻ')

if x % 2: # x % 2 -> 1 = Truthy
    print(x, 'là số lẻ')
else: # x % 2 -> 0 = Falsy
    print(x, 'là số chẵn')

"""
x % 2 có 2 khả năng:
- 0 -> Là số chẵn (Falsy)
- 1 -> Là số lẻ (Truthy)
"""

s = input('Nhập vào 1 dòng:')
print('Dòng nhập vào là:', s)
if s: # Truthy
    print(s, 'không rỗng')
else: # '' -> Falsy
    print('Dòng nhập vào rỗng')
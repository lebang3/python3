"""
2. Câu lệnh
Câu lệnh là các đơn vị thực thi nhỏ nhất của chương trình

Việc lập trình chính là viết các câu lệnh - liên kết chặt chẽ chúng với nhau theo 1 thứ tự phù hợp để giải quyết tự động vấn đề nào đó

print('Hello world') # lenh in ra man hinh
x = 5 # lenh gan
"""

"""
2.1 Lệnh nhập xuất dữ liệu
2.1.1 Lệnh in
- print dùng để in ra màn hình
- Có thể in ra 0, 1, 2, ... giá trị truyền vào - có thể khác kiểu dữ liệu
- in được biến
"""

print(1)
print('Hello')
print(2.2)

print(3, 4)
print('x:', 5)

x = 4
print('x:', x, 'x + 4:', x + 4)

"""
Tại sao lệnh print lại in ra được biến?

x = 4

-> print('x:', 4, 'x + 4:', 8)
"""

"""
2.1.1 Lệnh nhập từ bàn phím
-> input()
-> input('string hướng dẫn nd nhập vào: ')

"""

"""
Bài tập:
1. In ra dòng chữ "what's your name?'
2. Nhập vào tên và lưu trong biến my_name
3. in ra dòng chữ: tên của tôi là ...
"""

my_name = input('What is your name?')
print('My name is:', my_name)

x = input('Nhập vào 1 số nguyên:')
print(x, type(x))
# print(x + 5)

y = int(x)
print(y, type(y), y + 4)


x = int(input('Nhập vào 1 số nguyên: '))
print(x, type(x))
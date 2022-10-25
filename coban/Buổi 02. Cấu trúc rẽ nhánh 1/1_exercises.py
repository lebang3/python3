"""
Bài 3

-> Chaining operator
Toán tử so sánh chuỗi

(x > a) and (x < b)
-> Viết gọn lại: a < x < b
"""

x = float(input('Enter a number: '))
print('x la so duong: ', x > 0)
print('x la so am: ', x < 0)
print('x la so chan: ', x % 2 == 0)
print('x la so le: ', x % 2 != 0)
# print('x trong khoang 22-44: ', (x > 22) and (x < 44))
# print('x ngoai khoang 22-44: ', (x < 22) or (x > 44))
print('x trong khoang 22-44: ', 22 <= x <= 44)
print('x ngoai khoang 22-44: ', (x <= 22) or (x >= 44))

"""
Bài 4.
"""

c = input('Enter a character: ')

c_is_numeric = '0' <= c <= '9'
print(c, 'là ký tự số?', c_is_numeric, type(c_is_numeric))

c_is_lower = 'a' <= c <= 'z' ### ...
print(c, 'là chữ cái thường?', c_is_lower, type(c_is_lower))

c_is_upper = 'A' <= c <= 'Z' ### ...
print(c, 'là chữ cái hoa?', c_is_upper, type(c_is_upper))

"""
Ký tự đặc biệt
Đồng thời thỏa mãn 3 điều kiện
- 0 phải là ký tự thường a-z
- 0 phải ký tự hoa A-Z
- 0 phải số 0-9
=======
Nếu không phải là ký tự đặc biệt
-> Phải là
    hoặc ký tự thường
    hoặc ký tự hoa
    hoặc số
"""

is_not_special_char = c_is_numeric or c_is_lower or c_is_upper

print(c, 'là ký tự đặc biệt?', not is_not_special_char)

c_is_enter = (c == '')
print(c, 'là dấu enter?', c_is_enter)
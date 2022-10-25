"""
Một phương pháp cho phép nhúng biểu thức vào trong string

tính toán biểu thức và trả về giá trị -> nhúng kết quả vào trong string

Cú pháp:
- f'... {expression} ...'

-> Generate HTML động

lấy dữ liệu -> gắn vào trang html -> trả về kết quả

-> Template Engine 
    - lấy dữ liệu, format string vào trong trang html và trả kết quả
    - Java: Thymeleaf
    - Python: Jinja2
    - Ruby on Rails: ERB

Pypi
"""

s = f'abc mnk {2 + 3}, {5 * 6}, {1 + 2 * 3}'

x = 5
y = 7

s1 = f'abc mnk {x} {x + 2*y}'

print(s, type(s), id(s))
print(s1, type(s1), id(s1))

"""
s.format(1, 2, 3) => Format string
========
s % (1, 2, 'a') => C-style string interpolation
"""
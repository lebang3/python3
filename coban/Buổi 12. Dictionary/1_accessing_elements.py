"""
Truy cập - gán lại value theo key
bằng dấu []
==========
nếu truy cập vào key không tồn tại -> báo lỗi
"""

d3 = {
    'a': 1,
    'b': 2,
    'a': 5,
    1: 'a',
    2.2: 1,
    ('a', 'b'): ['a', 1]
}

print(d3['a'])
print(d3[('a', 'b')])

d3[('a', 'b')] = 10
print("d3",d3)

# print(d3[2.3])

"""
2.2 Phương thức get
-> chỉ dùng để lấy dữ liệu - không gán lại
-> khi không có key không báo lỗi
    -> trả về None 
    -> trả về giá trị quy định trong hàm
"""

test_var = d3.get(2.3)
print(test_var)

test_var = d3.get(2.3, 'Not exists')
print(test_var)

test_var = d3.get(2.3, -1)
print(test_var)
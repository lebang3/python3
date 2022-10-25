s1 = 'mnk'
s2 = '123abc'

print(s1 + s2)
print(s1 * 3)
print(s1 + 2 * s2)

s3 = 'abc mnk-xyz'
# Số phần tử của chuỗi
print(s3, len(s3))

"""
Hàm split trả về list các element được phân tách bằng
- mặc định k truyền vào gì: split = dấu space
- truyền vào split bằng dấu được truyền vào
"""
print(s3.split('-'))
print(s3.split())

"""
join là phiên bản ngược lại của split. Cho phép nối các chuỗi trong 1 list = dấu được join
"""

l = s3.split('-')
print(l)
print(' '.join(l))

# kiểm tra chuỗi con nằm trong chuỗi
print('abc' in s2)
print('a' in s1)
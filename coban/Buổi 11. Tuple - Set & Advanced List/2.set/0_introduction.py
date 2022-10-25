"""
Khai báo:
- sử dụng dấu {}
- set rỗng phải dùng hàm set()
"""

s = {1, 2, 5, 6}
print(s, type(s))

s1 = set()
print(s1, type(s1))

"""
Một vài phương thức thường gặp
- add 
- remove: xóa 1 phần tử truyền vào
- pop: xóa 1 phần tử bất kỳ
"""

s1.add(2)
print(s1)

s1.update([2, 3, 4, 5]) # list hoặc tuple, ...
print(s1)

s1.discard(3)
print(s1)

a = s1.pop()
print(a, s1)
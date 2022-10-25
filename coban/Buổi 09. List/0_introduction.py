"""
List là 1 kiểu dữ liệu phức hợp
- Chuỗi các phần tử nối tiếp nhau
- Mỗi phần tử thuộc 1 hoặc có thể nhiều kiểu dữ liệu khác nhau
- Có thể truy cập ngẫu nhiên dựa trên index
"""

"""
Khai báo list

>>> l = [1, 2]
>>> print(l, type(l))
[1, 2] <class 'list'>

>>> l1 = []
>>> print(l1, type(l1))
[] <class 'list'>

>>> l2 = [l1, 2, 3, 'abc', {'a': 1}]
>>> print(l2, type(l2))
[[], 2, 3, 'abc', {'a': 1}] <class 'list'>
"""

l1 = [1, 1.2, 3]
print(l1)
l2 = ['sb', 2, [2,3] ]
print(l2)

"""
>>> l1 + l2
[[], 2, 3, 'abc', {'a': 1}]
>>> l + l2
[1, 2, [], 2, 3, 'abc', {'a': 1}]
>>> l * 5
[1, 2, 1, 2, 1, 2, 1, 2, 1, 2]
"""

"""
>>> len(l)
2
>>> l.append(3)
>>> l
[1, 2, 3]
>>> len(l)
3
>>> l.insert(0, 0)
>>> l
[0, 1, 2, 3]
>>> print(l, len(l))
[0, 1, 2, 3] 4

>>> l.extend(l2)
>>> print(l, len(l))
[0, 1, 2, 3, [], 2, 3, 'abc', {'a': 1}] 9
"""

l = []
n = int(input('Nhap vao so n: '))
for _ in range(n):
    l.append(0)
print(l)

b = []
for i in range (1, n+1):
    b.append(i) # hoac i + 1
    # hoac range(1, n+1)
print(b)

c = []

## Cách 1
for i in range(1, n * 2):
    if i % 2:
        c.append(i)
    
print(c)

# Cách 2
c1 = []
for i in range(n):
    c1.append(i * 2 + 1)

print(c1)
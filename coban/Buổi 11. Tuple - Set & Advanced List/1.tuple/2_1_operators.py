t1 = (1, 2, 3)
print(t1, type(t1))

t2 = ('a',)
print(t2, type(t2))

"""
Phép cộng, nhân, truy cập phần tử
- cộng 2 tuple: nối như nối str
- nhân với 1 số: nhân tuple lên n lần như str
- truy cập phần tử: t[index]

=> Sử dụng lặp với tuple giống như list với lặp
- lặp bằng phần tử
- lặp bằng chỉ số
- lặp cả phần tử và chỉ số
"""

print(t1 + t2)
print(t1 * 3)
print(t1[2])

"""
t = (1, 2, 3, 4, 5)
=> Thay 2 phần tử đầu là 100 vào
=> in ra kết quả
"""

t = (1, 2, 3, 4, 5)
print((100, 100) + t[2:])
print(t[2:], type(t[2:]))
result = 100, 100, *t[2:]
print(result, type(result))

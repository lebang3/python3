"""
Vòng lặp for -> Cấu trúc lặp xác định
cú pháp:
- for i in range(10):
    ...
- for item in list_items:
    ...
Zero-indexing based -> Thường đếm index từ 0 trở đi -> range(N) -> 0 - N-1

Dùng dấu gạch dưới -> nếu vòng lặp không cần dùng đến chỉ số lặp
"""
for i in range(10): # 0 - 9
    print(i)

for _ in range(10):
    print('Hello world!')

"""
Bài 1: Nhập vào số N, in ra các số từ 1 - N dùng vòng lặp. Biểu diễn
bằng sơ đồ khối
"""

N = int(input("Nhập số N:\n"))
for i in range(N):  
    print(i+1)

for i in range(N):
    print('Hello world', i + 1)

"""
Đề bài: Nhập vào số n - tính tổng từ 1 đến n
-> vẽ lại sơ đồ khối của phép tính này bằng vòng lặp
"""

p = 1

for i in range(N):
    p *= i + 1

print(p)

sum_square = 0

for i in range(N):
    sum_square += (i+1) ** 2
    print('---------')
    print(i, sum_square)

print(sum_square)
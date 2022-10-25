"""
Mảng lồng nhau:
- Mảng nằm trong mảng
+ mảng 2 chiều
[[1, 2, 3], [2, 5, 6], [7, 2, 1]]
+ mảng 3 chiều
[
    [[1, 2, 3], [1, 2, 3], [1, 2, 3]], 
    [[1, 2, 3], [1, 2, 3], [1, 2, 3]], 
    [[1, 2, 3], [1, 2, 3], [1, 2, 3]]
]
+ Có thể mở rộng lên mảng n chiều

-> Biểu diễn ma trận(n >= 2), biểu diễn tensor(mảng nhiều chiều n >= 3)
"""

l = [[1, 2, 3], [2, 5, 6], [7, 2, 1]]
print(l[1])
print(l[0][1], l[2][2])

"""
Viết chương trình
Nhập vào một ma trận các số thực cỡ m * n với m, n nhập vào từ bàn phím
- In ra ma trận đó
- Tính tích của ma trận đó với x, với x là số thực nhập từ bàn phím
"""

# m hàng, n cột

while True:
    m = int(input('Nhập vào 1 số nguyên: '))
    n = int(input('Nhập vào 1 số nguyên: '))

    if m > 0 and n > 0:
        break

print(m, n)

l = []

for i in range(n):
    current_row = []
    for j in range(m):
        current_element = int(input(
            f'Nhập vào phần tử hàng {i + 1}, cột {j + 1}:'))
        current_row.append(current_element)
    l.append(current_row)

print(l)
print(l[1], l[0])

x = float(input('Nhập vào 1 số thực: '))

for i in range(n):
    for j in range(m):
        l[i][j] *= x

print(l)
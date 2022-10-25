"""
Viết chương trình:
- Nhập vào n nguyên dương
- Hỏi người dùng nhập vào n cặp key, value, với key là string còn value là số float
- In ra các key dưới dạng key1-key2-key3 (cách nhau bởi -)
- In ra tổng các values
"""

while True:
    N = int(input('Enter a positive values:'))

    if N > 0:
        break

    print('Invalid input', N)

d = {}

for i in range(N):
    key = input('Enter key ' + str(i + 1) + ': ')
    val = float(input('Enter value ' + str(i + 1)+ ': '))
    d[key] = val

print(d)
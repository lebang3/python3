"""
Nhập vào 1 số N
In ra: 
... là số chẵn (nếu N chẵn)
... là số lẻ (nếu N lẻ)
==========
Nhập vào số nguyên N:
Nếu N là số âm, in ra N là số âm. Ngược lại in ra N >= 0
In ra giá trị tuyệt đối của N
"""

n = int(input('Enter the number: '))
if n % 2 == 0:
    print(n, ' la so chan')
else:
    print(n, 'la so le')

result = n

if n < 0:
    result = -n
    print(n, 'la so am')
else:
    print(n, 'la so khong am')

print('Gia tri tuyet doi cua', n, 'la', result)

"""
Nhập vào số nguyên n (n != 0). In ra tất cả các ước số của n
"""

n = int(input('nhap vao so n :'))
for i in range(1, n+1):
    if n % i == 0 :
        print(i)


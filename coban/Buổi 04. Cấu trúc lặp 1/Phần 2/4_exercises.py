"""
1. Số nguyên tố là số chỉ có 2 ước là 1 và chính nó. Nhập vào 1 số n,
kiểm tra n có phải là số nguyên tố hay không

2. Nhập vào a, b - liệt kê các số nguyên tố trong khoảng a - b
"""

n = int(input( ' nhap  vào so n :'))

count = 0

for i in range(1, n + 1):
    if n % i == 0:
        count += 1

if count == 2:
    print(n, 'là số nguyên tố')
else:
    print(n, 'không phải số nguyên tố')


"""
N = a * b

1 ------------ sqrt(n) ------------ N
       a         -           b

a <= sqrt(n) => b >= sqrt(n)
"""
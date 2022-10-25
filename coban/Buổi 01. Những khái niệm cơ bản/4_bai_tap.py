"""
Viết chương trình:
Nhập vào 2 số a, b. In ra kết quả phép tính +, -, *, / của 2 số đã nhập
vào
    - Chỉ kết quả
    - Phép tính tường minh: a + b = 2.3 + 3.2 = 5.5

-) +, * (2 phút)
-) -, / (2 phút)
"""

x = float(input('Enter a float: '))
y = float(input('Enter a float: '))

print(x + y)
print('x + y =', x, '+', y, '=', x + y)

"""
Nhập vào số nguyên N, in ra kết quả tổng 1, 2, ..., N bằng công thức
N*(N+1)/2
"""

N = int(input('Enter a integer N: '))

"""
int(input('Enter a integer N: '))

-> input('Enter a integer N: ')| nhap vao 10
Tra ve '10'

-> int('10') -> ep kieu ve kieu so nguyen 
Tra ve 10

-> N = 10
"""

print('N:', N)
s = N * (N+1) // 2
print('Tong 1->N:', s)
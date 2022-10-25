"""
Nhập vào 1 số. 

Kiểm tra xem số đó có phải snt hay không?

-> Đặt biến is_prime làm cờ, giả định ban đầu số đó là snt

-> Khi gặp trường hợp k phải là snt (phát hiện ra 1 ước) -> gán lại cờ is_prime = False, break vòng lặp

-> kiểm tra biến is_prime và kết luận
"""

n = int(input("nhap vao so can kiem tra:"))

is_prime = True

if n == 1:
    is_prime = False

for i in range(2, n): # 9
    print('-----------')
    print(i)
    if n % i == 0:
        is_prime = False
        break
    print(is_prime)

if is_prime:
    print(n, 'là số nguyên tố')
else:
    print(n, 'không phải snt')

n = int(input("nhap vao so can kiem tra:"))

count = 0 

for i in range(1, n + 1):
    print('----------')
    print(i)
    if n % i == 0:
        print(i, 'là ước số')
        count = count + 1
    print('count', count)

if count > 2:
    print(n, "khong phai la so nguyen to")
else:
    print(n, "la so nguyen to")
"""
Tính tổng các số không phải số nguyên tố từ trong khoảng [2, n] sử dụng continue với n nhập từ bàn phím.
"""

"""
xét range(2, n + 1)
- với mỗi số i
    - nếu là snt -> cộng tổng
    - không là snt -> sử dụng continue để bỏ qua
"""

"""
Khi gặp continue -> phần bên dưới k được thực thi nữa
"""

n = int(input('Nhập vào 1 số n:'))

s = 0

for i in range(2, n + 1):
    count = 0 
    for j in range(1, i + 1):
        if i % j == 0:
            count = count + 1

    if count == 2:
        continue
    
    print(i) # i là các số không phải snt
    s += i

print('result', s)
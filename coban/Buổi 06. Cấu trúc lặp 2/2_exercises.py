"""
log10(1234) + 1 = 3,09131516 + 1
= 4.09
4 chữ số (làm tròn xuống)
==========
"""
import math

N = int(input('Nhập 1 số nguyên dương N: '))
N_copy = N
# Phần 2
m = math.floor(math.log10(N) + 1)

# ceil -> làm tròn lên
# floor -> làm tròn xuống
# round -> Làm tròn theo quy tắc 0-0.5 (xuống), còn lại là lên
print(m)

count = 0
s = 0

so_dao_nguoc = 0

while N != 0:
    print('-----------')
    print(N)
    count += 1
    don_vi = N % 10
    s += don_vi
    N = N // 10
    so_dao_nguoc += don_vi * 10**(m - 1)
    print('After', N, don_vi, count, don_vi * 10**(m - 1))
    m -= 1
# Phần 3
print('Số chữ sô', count)

# Phần 4
"""
- 0: Falsy
- 1, 2: Truthy
"""

if s % 3:
    print(N_copy, 'không chia hết cho 3')
else:
    print(N_copy, 'chia hết cho 3')

if s % 9 == 0:
    print(N_copy, 'chia hết cho 9')
else:
    print(N_copy, 'không chia hết cho 9')

print(so_dao_nguoc)

if N_copy == so_dao_nguoc:
    print(N_copy, 'là số đối xứng')
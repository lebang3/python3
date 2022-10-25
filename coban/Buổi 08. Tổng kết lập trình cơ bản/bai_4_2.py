m = int(input('Nhap chieu cao: '))
n = int(input('nhap do rong: '))
s = '*'

for _ in range(m):
    print(s * n)

s = '*'
r = ' '
print(s*n)

for _ in range(m-2):
    current_line = '*' + ' ' * (n-2) + '*'
    print(current_line)
print(s*n)

for i in range(m):
    print(' ' * i + '*')

print('----------')

for i in range(m):
    print(' ' * (m-i-1) + '*')
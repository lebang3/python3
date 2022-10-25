"""
1. In ra các vị trí trên bảng mã ascii của từng ký tự trong một string dưới dạng List
[65, 66, 67]
==============
2. Nhập vào duy nhất 1 ký tự chữ cái - sai yêu cầu nhập lại
- Nếu là ký tự thường -> đổi thành chữ hoa r in ra
- Chữ hoa thì in ra luôn kết quả
=> Thuần túy sử dụng hàm ord - chr (không dùng hàm khác của str trong python)
"""

s = 'abc234#$^&^'

l = []

for i in range(len(s)):
    l.append(ord(s[i]))

print(l)


while True:
    s = str(input('Nhap vao chu cai: '))
    if len(s) == 1 and (('a' <= s <= 'z') or ('A' <= s <= 'Z')):
        break
    print('Chi duoc nhap 1 chu cai')

print(s)

if 'a' <= s <= 'z':
    print(chr(ord(s) - 32))
else: 
    print(s)
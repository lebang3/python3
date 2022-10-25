"""
Viết chương trình:
Nhập vào 1 chuỗi kí tự, lưu ở biến s
Đổi các chữ cái về in thường, loại bỏ các kí tự không phải số và
không phải chữ, in ra chuỗi kí tự đã xử lý

-> abcDDDDAAb$$a012aA
-> abcddddaaba012aa

"""

s = input('Nhap vao chuoi ki tu: ')
b = []

for c in s:
    if 'A' <= c <= 'Z':
        b.append(chr(ord(c) + 32))
    elif 'a' <= c <= 'z' or '0' <= c <= '9':
        b.append(c)
    else: 
        continue

print('-'.join(b))


s = 'quaCh hUy TunG'

tmp = ''

for c in s:
    if 'A' <= c <= 'Z':
        tmp += chr(ord(c) + 32)
    else:
        tmp += c

l = []

for w in tmp.split():
    l.append(chr(ord(w[0])-32) + w[1:])
    # w.capitalize()
    # l.append(w.capitalize())

print(' '.join(l))
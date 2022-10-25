"""
Viết chương trình:
- Nhập vào 1 chuỗi kí tự tiếng anh, lưu ở biến s
- Nhập vào 1 ký tự và lưu tại biến x

- Đếm số lần xuất hiện của x trong s
- Tìm kiếm tất cả vị trí kí tự x trong chuỗi. Nếu không tìm thấy in ra -1

- Tìm kiếm vị trí đầu tiên xuất hiện kí tự x từ bên trái sang phải, từ phải sang trái, nếu không tìm thấy in ra -1
"""

s = input('Nhập vào 1 chuỗi: ')
x = input('Nhập vào 1 ký tự: ')

print(s, x)

a = 0
l = []

for i,c in enumerate(s):
    if x == c:
        a += 1
        l.append(i + 1)

if a != 0:
    print('So lan xuat hien cua x la: ', a)
    print(l)
else:
    print(-1)

b = [] 

for i in range(len(s)):
  if s[i] == x:
    b.append(i)

if len(b) == 0:
    print(-1)
else:
    print('Vi tri dau tien cua x la: ', b[0] + 1)
    print('Vi tri dau tien cua tu ben phai x la: ', b[-1] + 1)

"""
Tìm kiếm vị trí đầu tiên xuất hiện kí tự đó từ bên trái sang phải, từ
phải sang trái, nếu không tìm thấy in ra -1
"""

# Tìm từ bên trái sang

pos_from_left = -1

for i,c in enumerate(s):
    if c == x:
        pos_from_left = i + 1
        break

print(pos_from_left)

pos_from_right = -1

for i,c in enumerate(s[::-1]):
    if c == x:
        pos_from_right = len(s) - i
        break

print(pos_from_right)


pos_from_right_2 = -1
for i,c in enumerate(s):
    print('----------')
    print(i, c, c == x)
    if c == x:
        pos_from_right_2 = i + 1
    print(pos_from_right_2)
print(pos_from_right_2)

"""
Btvn
Bài xử lý chuỗi
Bài xử lý chuỗi tiếp

Trang 20/21 trên slides
"""
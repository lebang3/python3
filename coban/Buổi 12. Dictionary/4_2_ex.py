"""
Viết chương trình
Khởi tạo một dictionary, có key là a - z, value đều là 0. In ra dict đó
Nhập vào một chuỗi họ tên không dấu, in ra chuỗi đó
In ra mỗi kí tự đã xuất hiện bao nhiêu lần sử dụng dict đã khai báo ở
câu a
=======
không phân biệt hoa - thường
"""

d2 = {chr(ord('a') + i): 0 for i in range(26)}
print(d2)

s = input('Nhap vao ten cua ban: ')
print(s)

s = s.lower()
print(s)

for c in s:
    if c == ' ':
        continue

    d2[c] += 1

for k, v in d2.items():
    if v != 0: # có tồn tại phần tử k
        print(k, v)
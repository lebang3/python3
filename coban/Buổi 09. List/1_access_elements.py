"""
1.1 Chỉ số mảng

Phần tử     :         a   b   1   2   m   c 
Chỉ số dương:         0   1   2   3   4   5
Chỉ số âm   :        -6  -5  -4  -3  -2  -1

=> Đa số tính chỉ số cho mảng từ 0, 1, 2, ..., len - 1
=> nếu truy cập ngoài pt của mảng, báo index error
    print(l[7])
IndexError: list index out of range

=> Chỉ số âm: -1, -2, ...., -len(l)


"""

l = ['a', 'b', 1, 2, 'm', 'c']
print(l[0], l[3], l[5])
# print(l[7])

print(l[len(l) - 1])
print(l[len(l) - 3])
print(l[len(l) - 5])

print(l[-3])
print(l[-5])


for i in range(len(l)): # i: 0, 1, 2, ..., len-1
    print(i, l[i])

"""
Nhập 1 số n nguyên dương, yêu cầu nhập lại đến khi đúng. 
Nhập 1 mảng gồm n số. kí hiệu biến a

Yêu cầu:
- copy a sang list b, sử dụng lặp và hàm append
- copy a sang list c, đảo ngược thứ tự, sử dụng hàm insert + vòng lặp
- copy a sang list d, đảo ngc thứ tự, dùng hàm append + vòng lặp
"""

# while True:
#     n = int(input('Moi nhap so nguyen duong:'))
#     if n>0:
#         break
#     print('So khong hop le')


# a = []
# b = []
# c = []

# for _ in range(n):
#     a.append(int(input()))
# print(a)

# for i in range(len(a)):
#     b.append(a[i])
# print(b)

# for i in range(len(a)):
#     c.insert(0, a[i])
# print(c)

# d = []
# for i in range(1, len(a) + 1):
#     d.append(a[-i])

"""
Slicing

Phần tử     :         a   b   1   2   m   c 
Chỉ số dương:         0   1   2   3   4   5
Chỉ số âm   :        -6  -5  -4  -3  -2  -1


"""
print(l[1:5])
print(l[1:5:2])

# print(l[-5:-2])
# print(l[-5:-2:1])
print(l[-2:-5:-1])

# print(l[-5:5:2])
# print(l[1:-1])
# print(l[1:-1:2])
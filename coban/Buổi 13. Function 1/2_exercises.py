"""
Bài 1: Viết 1 hàm, kiểm tra 1 số là số nguyên tố hay không? -> Trả về bool (True/False)
(5 phút)

Bài 2: Viết chương trình
- Nhập vào 2 số a, b nguyên dương
- tạo ra 1 list, lưu các số nguyên tố trong khoảng [a, b] vào mảng đó
- In ra tổng các phần tử trong list

(5 phút)
"""

def is_snt(N):
    if N == 1:
        return False

    count = 0
    
    for i in range(1, N + 1):
        if N % i == 0:
            count += 1

    if count == 2:
        return True
    else:
        return False

# print(is_snt(11), is_snt(21), is_snt(31))

while True:
    a = int(input('Nhập vào 1 số nguyên dương: '))
    b = int(input('Nhập vào 1 số nguyên dương: '))

    if a > 0 and b > 0 and a <= b:
        break

    print('Nhập vào sai')

result = []
s = 0
for i in range(a, b + 1):
    if is_snt(i):
        result.append(i)
        s += i

print(result, sum(result), s)
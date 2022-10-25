"""
Tính tổng các số lẻ từ a - b với a, b
nhập vào từ bàn phím. Nếu gặp một
số nguyên tố thì dừng ngay việc tính
tổng và in ra kết quả
"""

"""
Khi vòng lặp gặp lệnh break
-> thoát ra khỏi vòng lặp hiện tại - k xét tiếp nữa
"""

a = int(input('Nhập vào a:'))
b = int(input('Nhập vào b:'))

s = 0

for i in range(a, b + 1):
    print('------------')
    print(i)
    ### Kiểm tra i là snt hay không
    count = 0 

    for j in range(1, i + 1):
        if i % j == 0:
            count = count + 1

    if count == 2: # là snt
        print(i, 'snt')
        break

    if i % 2:
        s += i

    print(s)

print(s)
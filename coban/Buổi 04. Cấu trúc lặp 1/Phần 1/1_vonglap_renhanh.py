"""
1. Vong lap + re nhanh
- Các sơ đồ khối từ trước đến giờ: khối thoi (rẽ nhánh) chỉ dùng để kết thúc (thoát khỏi vòng lặp)

-> if
    - true: tiếp tục lặp
    - false: thoát khỏi vòng lặp
----------------
Mở rộng
-> if
    - true:
        - xử lý 1
        - xử lý 2
        - if 2(rẽ nhánh)
        ...
    - false
        - kết thúc lặp
"""

s = 0

for i in range(11):
    if i % 2:
        s += i
    print(i, 'kiem tra i la so le', i % 2 == 1)
    print(s)

print('Tong so le 0 - 10:', s)

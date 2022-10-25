"""
Btvn 1
Nhập vào số nguyên dương n (giả định ng dùng luôn nhập đúng - không
cần kiểm tra) Tiếp theo, nhập n số từ bàn phím.
Hỏi:
- Số lớn nhất là số nào, nằm ở vị trí nào
- Số nhỏ nhất nằm ở vị trí nào, là bao nhiêu
"""

"""
min_i = min(min_(i-1), current)
max_i = max(max_(i-1), current)

-> khởi tạo 1 giá trị ban đầu
-> Gán lại khi cần phải thay đổi
-> Chạy đến cuối -> kết quả chính xác cuối cùng
"""
import math

while True:
    n = int(input('Nhập vào số n: '))
    if n > 0:
        break

print(n)

min_value = math.inf # sô lớn nhất có thể
max_value = -math.inf # sô nhỏ nhất có thể

count_min = 0
count_max = 0

for i in range(n):
    current = float(input('Nhập vào 1 số: '))

    if current > max_value:
        count_max = i + 1
        max_value = current
    
    if current < min_value:
        count_min = i + 1
        min_value = current
    

print('Min', min_value, 'position:', count_min)
print('Max', max_value, 'position:', count_max)
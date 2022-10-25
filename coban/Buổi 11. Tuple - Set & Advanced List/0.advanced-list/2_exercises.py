"""
Nhập vào n phần tử nguyên dương, với n nhập vào từ bàn phím
Hỏi có bao nhiêu phần tử phân biệt trong list số đã nhập
Mỗi số xuất hiện bao nhiêu lần
"""

"""
Sử dụng mảng đếm phần tử

Index              :    0   1   2   3   4   5   6
Giá trị của mảng   :    0   0   2   1   3   0   1

-> Sử dụng index của mảng biểu diễn các phần tử
-> Sử dụng giá trị tương ứng index -> biểu diễn số lần xuất hiện của phần tử đó


"""
import math

n = int(input('Nhập vào số n: '))
l = [int(input(f'Nhập vào số thứ {i+1}: ')) for i in range(n)]
print(l)

max_value = -math.inf

for item in l:
    if item > max_value:
        max_value = item

print(l, max_value)

result = [0 for _ in range(max_value + 1)]
for item in l:
    result[item] += 1
    
print(result)

for idx, item in enumerate(result):
    if item != 0: # số có lần count >= 1
        print(idx, item)
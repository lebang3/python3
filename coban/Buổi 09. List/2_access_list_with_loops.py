l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

## Truy cập bằng chỉ số:
for i in range(len(l)):
    print(i, l[i])

print('------------')
# Truy cập bằng phần tử:
for item in l:
    print(item)

print('------------')
for idx, item in enumerate(l):
    print(idx, item)

"""
Nhập vào số n, nhập vào list n phần tử số thực. Hỏi:
- Tổng các số trong list là bao nhiêu
- Phần tử lớn nhất - nhỏ nhất có vị trí nào, giá trị bao nhiêu
"""
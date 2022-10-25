
"""
Nhập vào hai số nguyên a, b (a < b). Hãy đếm số số lẻ
trong đoạn [a, b]
"""
a = int(input('Nhập vào số a: '))
b = int(input('Nhập vào số b: '))

count = 0
for i in range(a, b + 1): # 0 - n (nếu xét range(n+1))
    print('-------------------')
    print('i', i)
    if i % 2: # tương đương i % 2 == 1
        # Tính chất truthy - falsy
        # i % 2 -> 0 False -> là số chẵn
        # i % 2 -> 1 True -> Là số lẻ
        count = count + 1
    print(count)

print(count)
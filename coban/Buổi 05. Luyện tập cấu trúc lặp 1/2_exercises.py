n = int(input())

for i in range(1, n + 1):
    for j in range(1, i + 1):
        print(i, end = ' ')
    print()

print('----------')

for i in range(1, n + 1):
    for j in range(1, i + 1):
        print('*', end = ' ')
    print()
print('----------')
for i in range(0, n):
    # print('+++++++')
    # print(i, n - i + 1)
    for j in range(0, n - i):
        print('*', end = ' ')
    print()

"""
Dòng đầu - in 4 dấu *
for j in range(0, 4)
-----------
Dòng 2 - in 3 dấu
for j in range(0, 3)
-----------
Dòng 3 - in 2 dấu
for j in range(0, 2)
-----------
Dòng 1 - in 1 dấu
for j in range(0, 1)

=> khi vòng lặp bên ngoài tăng chỉ số i
=> vòng lặp bên trong sẽ giảm số lần lặp

=> j in range(0, n - i)
"""
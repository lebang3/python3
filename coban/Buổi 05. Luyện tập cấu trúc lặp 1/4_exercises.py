n = 1000

s = 1

"""
break - continue luôn luôn ở trong bt điều kiện nào đó
"""

for i in range(1, n + 1):
    print('--------')
    print(i)
    giai_thua = 1

    for j in range(1, i + 1):
        giai_thua *= j

    if 1/giai_thua < 0.00000001:
        break

    s += 1/giai_thua
    print(giai_thua, 1/giai_thua, s)

print(s)
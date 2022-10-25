s1 = {1, 2, 3, 4, 5}
s2 = {i for i in range(4, 10)}

print(s1, s2)

"""
Phép toán thường gặp
- hợp 
- giao 
- phần bù
"""

print(s1.union(s2)) # hợp 2 tập hợp
print(s1.intersection(s2)) # giao 2 tập hợp
print(s1.difference(s2)) # trừ 2 tập hợp
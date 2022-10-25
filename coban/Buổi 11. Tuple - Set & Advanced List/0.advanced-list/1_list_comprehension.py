n = 100

# l = []
# for i in range(n):
#     l.append(0)
# print(l)

"""
List comprehension
- Là phương pháp khai báo list trong cùng 1 dòng
- Có thể lọc được phần tử (if phía sau)
- Có thể format phần tử (if phía trước)

=> Không nên viết list comprehension quá phức tạp -> khó đọc
- dùng 2 mệnh đề if để lọc + format phần tử
- list comprehension lồng nhau
"""

l = [0 for _ in range(n)]
print(l)

l1 = [i for i in range(n)]
print(l1)

l1_odd = [i for i in range(n) if i % 2]
print(l1_odd)

l1_odd_formatted = [i if i % 2 else i + 100 for i in range(n)]
print(l1_odd_formatted)

l1_odd_formatted_filter = [i if i % 2 else \
    i + 100 for i in range(n) if i % 3 == 0]
print(l1_odd_formatted_filter)

print([i for i in l1])
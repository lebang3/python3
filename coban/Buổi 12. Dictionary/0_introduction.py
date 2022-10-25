"""
Khởi tạo:
- d = {...}
- dictionary comprehension

=============
Tính chất dictionary
- Key:
+ phải thuộc các kiểu dữ liệu immutable (str, int, float, tuple)
+ không thể là các giá trị thuộc kiểu dữ liệu mutable (list, set, dictionary)

+ key phải không trùng nhau, nếu có trùng nhau, chỉ khai báo cuối cùng được chấp nhận

- Value:
+ không quan tâm đến value thuộc kiểu nào
"""
d = {
    'a': 1,
    'b': 2
}
print(d, type(d))
print(d['a'])
d['a'] = 30
d['c'] = 10
print(d)

d1 = {
   i: 0 for i in range(10) 
}
print(d1, type(d1))

"""
Khởi tạo dictionary d, có key từ 'a', 'b', . . . , 'z', value = 0(tất cả) theo 2 cách.
1 Sử dụng vòng lặp và gán từng key
2 Sử dụng dictionary comprehension
"""

# num = int(input("type num :"))

# d = {}

# for _ in range(num):
#     value = input("type value: ")
#     key = int(input("type key:"))
#     d.update({value:key})

# print(d)

d1 = {}

for i in range(26):
    current_char_index = ord('a') + i
    current_char = chr(current_char_index)
    # print(current_char_index, current_char)
    d1[current_char] = 0

print(d1)
print('----------')

d2 = {chr(ord('a') + i): 0 for i in range(26)}
print(d2)

print('------')
asciiDict = {chr(i + ord('a')): 0 for i in range(26)}
print(asciiDict)

d3 = {
    'a': 1,
    'b': 2,
    'a': 5,
    1: 'a',
    2.2: 1,
    ('a', 'b'): ['a', 1]
}

print(d3)
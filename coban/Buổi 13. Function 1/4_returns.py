"""
Return được sử dụng để trả về giá trị của function cho các lời gọi của nó
================
Lệnh return trả về giá trị và kết thúc hàm ngay lập tức
-> có thể dựa vào tính chất đó để điều khiển hàm
Ví dụ:
def is_snt(N):
    if N == 1:
        return False
===============
Các giá trị có thể return

- 1 giá trị: int, str, float, dictionary, ...
- 0 giá trị nào -> return None
    - Thường được sử dụng để kết thúc hàm - hàm đệ quy
    - Thường kết hợp với if else
- nhiều giá trị: -> không phải, return 1 tuple được packing (sử dụng t.c của tuple)
"""

def func():
    return 10
    # abc = 10
    # de = 15
    # print(abc + de)

print(func(), func() + 5)

def func_2():
    abc = 10

    return

    de = 15
    print(abc + de)

print(func_2())

def func_3():
    return 2, 3, 5, 'a' # packing tuple


a, b, c, d = func_3()
print(a, b, c, d)

a1 = func_3()
print(a1, type(a1))

a, *b, c = func_3()
print(a, b, c)

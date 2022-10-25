"""
Recursive - Đệ quy
==================
def func2():
    pass
def func1():
    # func2()
    ## other things
    func1()
func1()
- Hàm đệ quy là hàm gọi đến chính nó
- Có điều kiện đầu để kết thúc lời gọi đệ quy
==========
Các bài toán phát biểu đệ quy

Tính 2 ^ n với n nhập vào từ bàn phím
"""

"""
Callstack
===============
"""

def func2():
    x = 5
    print('Hello from func 2')
    y = 10
    x = x + y
    print('Goodbye from func 2')

def func1():
    print('Hello from func 1')
    func2()
    print('Goodbye from func 1')

print('Hello from main')
func1()
print('Goodbye from main')
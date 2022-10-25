"""
lambda function: hàm nặc danh
---------------
lambda param1, param2: (return)

-> inline function: khai báo trên cùng 1 dòng
"""

def func13(a, b):
    return a + b

print(func13(1, 2))

func_21 = lambda a, b: a + b

print(func_21(10, 15))

print(func13, type(func13))
print(func_21, type(func_21))


def execute_this(func_obj, x, y):
    print(func_obj(x, y))


execute_this(func13, 3, 5)
execute_this(func_21, 3, 5)
execute_this(lambda x, y: x + y, 3, 5)
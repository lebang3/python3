"""
Function 1: (95 % cách sử dụng thông thường)
- khai báo - sử dụng hàm
- tham số
- return
==================
Function 2: Hàm đệ quy 
(0.1% -> Sử dụng ở trong lúc đi học - làm việc với cấu trúc dữ liệu-giải thuật)
==================
Function 3: Variadic function + Lambda function (10%)
"""

### Variadic function
print(max(10, 15))
print(max(10, 15, 20, 25, 30))
print(max(10, 15, 20, 25, 30, 255, 30))

"""
Variadic func là hàm có thể truyền vào số lượng tham số tùy ý
---------
Khai báo
-> *args ở cuối khai báo danh sách tham số
-> args sẽ nhận dạng tuple
-> Truyền vào hàm khi gọi: số tham số >= số tham số bắt buộc. nếu = thì args là tuple rỗng

args chỉ là tên biến, có thể thay thế bằng bất cứ tên nào khác

===========
**kwargs

https://www.geeksforgeeks.org/args-kwargs-python/
"""

print(1, 2, 3, 'abc', 3, 4, 5)
print('Hello world')

def var_func_1(a, b, *x):
    print(a, b)
    print(x, type(x))

var_func_1(1, 2)
var_func_1(1, 2, 'a', 'b', 1, 2, 3)

"""
khai báo hàm my_sum, nhận số lượng tùy ý các tham số
trả về tổng các số nguyên, số thực đã nhập vào, bỏ qua các kiểu dữ liệu khác
"""

def my_sum(*arg):
    result = 0
    
    for item in arg:
        if type(item) == int or type(item) == float:
            result += item

    return result

print(my_sum(1,2,3,4, 'a', True, 10, 2.2))

def var_func_2(x, y, *args, **kwargs):
    print(x, y)
    print('------------')
    print(args, type(args))
    print('------------')
    print(kwargs, type(kwargs))

var_func_2(1, 2, 2, 3, 4, 5, 6, a=1, b=2, c=3)
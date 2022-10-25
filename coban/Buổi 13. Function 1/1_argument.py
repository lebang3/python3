"""
Danh sách tham số của hàm
=================
def + tên hàm (danh sách tham số):
    ....
    thân hàm
    ...
    trả về giá trị return
    ...
"""

def print_hello_n_times(n):
    print(n)
    for _ in range(n):
        print('Hello')

print_hello_n_times(10)
print_hello_n_times(2)

"""
Viết chương trình
- Nhập vào 1 số nguyên dương x
- Nhập vào string s

Viết hàm print_s_n_times, nhận vào 2 tham số: str để in ra, số lần in

In string s đã nhập vào n lần
"""

while True:
    n = int(input('Nhap vao n: '))
    if n > 0:
        break
    print('Nhap sai')
s = str(input('Nhap vao chuoi s: '))

def print_s_n_times(s,n):
    for _ in range(n):
        print(s)

print_s_n_times(s,n)

"""
Default argument
- Giá trị mặc định sẽ được ghi đè nếu có giá trị truyền vào vị trí đó
- Nếu không thì tham số nhận giá trị mặc định
==========
Vị trí của tham số mặc định nằm ở đâu trong danh sách các tham số
- đầu?
- giữa?
- cuối?
Tại sao lại như vậy, tại sao không ở các vị trí khác?

* Giả sử
def test(a=3, b=2, c):
    print(a, b, c)

test(5, 1, 3)
test(10)
test(10, 15)

-> Tham số mặc đinh phải ở cuối -> Nhập nhằng về ngữ nghĩa, không biết tham số nào nhận giá trị nào
===============
Bình thường, các function muốn gọi, số tham số cần gọi = số tham số truyền vào

Nếu là default args -> số tham số khi gọi hàm <= số tham số của hàm

Câu hỏi:
- nhỏ nhất, số lượng tham số là bao nhiêu
- lớn nhất là bn
- khi là giá trị min < x < max -> thì gán tham số cho function ntn

=> Khai báo 1 hàm, lấy ví dụ trong hàm thực tế đó
"""

def func_2(a, b, c = 3):
    print(a, b)
    print(c)

func_2(1, 2, 5)
func_2(5, 7)

def func_3(a, b, c=3, d='a', e=10):
    print(a, b, c, d, e)

func_3(10, 100) # min
func_3(10, 15, 20, 30, 50) # max

func_3(10, 15, 20)
func_3(10, 15, 20, 30)

"""
named argument
=> Tham số có tên

-> Truyền tham số vào hàm bằng chính tên của tham số đó, không quan tâm đến tính thứ tự
"""

func_2(b = 10, a = 1)

func_2(b = 10, c = 15, a = 1)
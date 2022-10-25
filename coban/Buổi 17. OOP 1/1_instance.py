class Cat:
    def __init__(self, mau_long):
        self.mau_long = mau_long

    def make_sound(self):
        print(id(self))
        print('Meow')

my_cat = Cat('den')
my_neighbor_cat = Cat('trang')

print(my_cat.mau_long)
print(my_neighbor_cat.mau_long)

"""
thuộc tính = biến của đối tượng
phương thức = hàm của đối tượng
"""

"""
Đối tượng
- thuộc tính -> instance attribute: khai báo trong hàm khởi tạo __init__ (biến của đối tượng)
- cú pháp def __init__(self, ...):
            self.abc = ...

- thuộc tính của đối tượng lưu trữ các thông tin riêng về đối tượng
==========
hành vi (phương thức)

class ...
    def my_method(self, ....):
        ....

=> tham số đầu tiên truyền vào phương thức là self, chính là đối tượng gọi phương thức đó
=> ngầm định -> không cần truyền vào nữa

"""

my_cat.make_sound()
print(id(my_cat))

"""
Khai báo lớp Cat2 :
- mỗi con mèo lưu trữ 2 thông tin: màu lông, màu mắt
- có hàm print_info(in ra id của con mèo + màu lông + màu mắt của con mèo đó)
"""

class Cat2: #Khai báo lớp Cat2 :
    def __init__ (self, mau_long, mau_mat): #mỗi con mèo lưu trữ 2 thông tin: màu lông, màu mắt
        self.mau_long = mau_long
        self.mau_mat = mau_mat
 
    def print_info(self):#in ra id của con mèo + màu lông + màu mắt của con mèo đó
        print(id(self), self.mau_long, self.mau_mat) 

c = Cat2('den', 'xanh')
c.print_info()
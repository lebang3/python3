

class MyClass:
    pass

a = MyClass()
b = MyClass()

print(a, type(a), id(a))
print(b, type(b), id(b))
print(a is b)

c = b
print(c is b)


"""
Tao ra nguyen mau -> class

class TenClass:
    ...


Tao ra doi tuong:

ten_bien = TenClass()
"""

"""
Ví dụ:
- Khai báo lớp con mèo, tạo ra 3 đối tượng: my_cat, my_neighbor_cat, wild_cat
- in ra 3 đối tượng đó, id + class của 3 đối tượng đó
"""


class Conmeo:
    pass
    
my_cat = Conmeo()
my_neighbor_cat = Conmeo()
wild_cat = Conmeo()
print(my_cat, type(my_cat), id(my_cat))
print(my_neighbor_cat, type(my_neighbor_cat), id(my_neighbor_cat))
print(wild_cat, type(wild_cat), id(wild_cat))
"""
- Tính chất OOP(2/4)
+ Encapsulation - đóng gói
+ Inheritance
- Luyện tập
"""

"""
Encapsulation
----------------
Có những thông tin, hành vi không nên được truy cập ở mọi nơi, người ta đóng gói chúng lại, chỉ cho phép truy cập nội bộ bên trong class

- Các thuộc tính/hành vi như vậy được gọi là private, bắt đầu bằng __ (2 dấu shift -)

----------------
Ý nghĩa:
- che giấu dữ liệu (attribute) - che dấu hành vi (method)
- !!! Chỉ đưa ra bên ngoài để mọi người biết đến 1 vài thứ quan trọng nhất
phần ở bên trong xử lý nôi bộ: 
+ dễ kiểm soát
+ không bị tác động, thay đổi dữ liệu từ bên ngoài
+ Không bị rối loạn cách hiểu (quá nhiều thứ có thể sử dụng -> không biết dùng cái nào)
"""

class Meow:
    default_color = 'unknown' # class attribute
    default_owner = 'unknown'

    def __init__(self, mau_mat, mau_long): # method
        if self.__validate_color(mau_mat): 
            self.mau_mat = mau_mat # instance attributes
        else:
            self.mau_mat = self.__class__.default_color
        
        self.set_mau_long(mau_long)

    def __repr__(self):
        return f'<Cat. mau_mat: {self.mau_mat}, mau_long: {self.__mau_long}>'

    def get_mau_long(x):
        return x.__mau_long

    def set_mau_long(self, mau_long):
        if self.__validate_color(mau_long):
            self.__mau_long = mau_long
        else:
            self.__mau_long = self.__class__.default_color 

        return self

    def set_owner(self, owner_name):
        if type(owner_name) != str:
            self.__owner = self.__class__.default_owner
        else:
            self.__owner = owner_name
        
        return self

    def get_owner(self):
        return self.__owner

    def __validate_color(self, mau):
        if type(mau) == str:
            return True
        return False

m1 = Meow('den', 'trang')
print(m1)

## m1.__validate_color('xanh') -> lỗi
## m1.__mau_long -> lỗi 

m2 = Meow(1, 2)
print(m1.get_mau_long()) 
m1.set_mau_long('vang')
print(m1)


"""
Lấy được thông tin biến private

- sử dụng getter (thường dùng để get các biến/attribute/thuộc tính của instance)
    def get_mau_long(self):
        return self.__mau_long

- setter:
    - validate dữ liệu
    - set dữ liệu trong attrib private


    def set_mau_long(self, mau_long):
        if self.__validate_color(mau_long):
            self.__mau_long = mau_long
        else:
            self.__mau_long = self.__class__.default_color 
"""

"""
Ví dụ:
Giả sử thông tin về chủ con mèo không được tiết lộ 

-> khai báo thuộc tính owner private cho lớp mèo
-> khai báo phương thức getter/setter cho thuộc tính này
"""

m1.set_owner('Quach Huy Tung') \
  .set_mau_long('tim')

print(m1, m1.get_owner())

"""
Tại sao nên return self trong setter?
----------
chaining operator

m1.set_owner('Quach Huy Tung') -> kết quả trả về là m1
m1.set_mau_long('tim') -> kết quả trả về là m1
"""
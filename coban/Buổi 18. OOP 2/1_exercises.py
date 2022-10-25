"""
- Khai báo lớp PhanSo, hàm khởi tạo nhận 2 giá trị tu_so, mau_so
- Getter, setter tử số, mẫu số. Biết mẫu số khác 0, cho phép set lại trong khi chạy
- Luôn luôn phải rút gọn phân số bằng hàm private - ngay khi khai báo
- Hàm khởi tạo gọi lại 3 hàm, set tử số, set mẫu số, rút gọn phân số

-> hàm __repr__, có thể in ra phân số
--------------------------------
- Phương thức cộng 2 phân số, trả về 1 đối tượng Phân số (làm trên lớp)

trừ nhân chia phân số
"""

import math

class PhanSo:
    def __init__(self, tu_so, mau_so):
        tu_so, mau_so = self.__rut_gon_phan_so(tu_so, mau_so)
        self.set_tu_so(tu_so)
        self.set_mau_so(mau_so)

    def get_tu_so(self):
        return self.__tu_so

    def get_mau_so(self):
        return self.__mau_so

    def set_tu_so(self, tu_so):
        self.__tu_so = tu_so

    def set_mau_so(self, mau_so):
        if mau_so == 0:
            raise Exception('Mẫu số phải khác 0')
        self.__mau_so = mau_so

    def __rut_gon_phan_so(self, tu_so, mau_so):
        common_factor = math.gcd(tu_so, mau_so)

        return tu_so // common_factor, mau_so // common_factor

    def __repr__(self):
        return f'{self.__tu_so}/{self.__mau_so}'

    def add_phan_so(self, other):
        tu_so = self.get_tu_so() * other.get_mau_so() + \
                    other.get_tu_so() * self.get_mau_so()

        mau_so =self.get_mau_so() * other.get_mau_so()

        return self.__class__(tu_so, mau_so)


a = PhanSo(1, 2)
b = PhanSo(6, 9)

print(a, b, a.add_phan_so(b))
# print(PhanSo(1, 0))
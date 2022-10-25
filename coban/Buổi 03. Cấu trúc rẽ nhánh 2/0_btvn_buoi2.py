"""
Năm nhuận
- Các năm bất đầu thế kỷ: 
    - 2000 (nhuận)
    - 2100 (không nhuận)
    - 2200 (không nhuận)
    - 2300 (không nhuận)
    - 2400 (nhuận)
- Trường hợp khác
    - chia hết cho 4 (nhuận)
    - còn lại (không nhuận)
=================
Biểu thức logic kiểm tra
- Hoặc là năm đó // 400 -> Nhuận
- Hoặc (năm đó chia hết cho 4 và không được chia hết cho 100) -> Nhuận
"""

x = int(input('Nhap vao 1 nam bat ky: '))

check_nam_nhuan = (x % 400 == 0) or ((x % 4) == 0 and (x % 100) != 0)

if check_nam_nhuan:
    print(x, 'la nam nhuan')
else:
    print(x, 'khong phai la nam nhuan')
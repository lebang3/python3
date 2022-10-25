"""
Bài 1: Kiểm tra x âm, dương, bằng 0 bằng điều kiện lồng nhau
"""

print('Bài 1')
x = int(input('Nhập vào 1 số nguyên: '))
print('Số vừa nhập vào là:', x)

if x <= 0:
    if x == 0:
        print('Số vừa nhập vào = 0')
    else:
        print(x, 'là số âm')
else: # x > 0
    print(x, 'là số dương')

print('Kết thúc bài 1')

"""
- Nhập vào hệ số a, b của phương trình ax + b = 0
- In ra nghiệm nếu có của phương trình - nếu không kết luận phương
trình vô nghiệm
"""
print('Bài 2:')
a = float(input('Nhập vào a: '))
b = float(input('Nhập vào b: '))

# if a == 0 and b != 0:
#     print ( ' phuong trinh vo nghiem ')
# elif a == 0 and b == 0:
#     print('Phương trình vô số nghiệm')
# else: #a != 0 
#     print ( ' phuong trinh co 1 nghiem la ' , -b/a )

if a == 0:
    if b == 0:
        print('Phương trình vô số nghiệm')
    else:
        print('Phương trình vô nghiệm')
else:
    print('phuong trinh co 1 nghiem la', -b/a)
print('Kết thúc bài 2')

"""
Bài 3: Tính cước taxi
"""

x = float(input("Nhập vào quãng đường khách muốn đi:\n"))

gia_km_dau = 15
gia_20_km_tiep_theo = 12
gia_21_km_tro_di = 10

cuoc_phi = 0
if x <= 1:
   cuoc_phi = gia_km_dau 
   print("Cước phí là: ", cuoc_phi)
else:
    cuoc_phi = gia_km_dau + gia_20_km_tiep_theo * (x-1)
    if x > 1 and x <= 21:
        print("Cước phí là: ", cuoc_phi)
    else:
        cuoc_phi += gia_21_km_tro_di * (x - 21) 
        ## cuoc_phi = cuoc_phi + gia_21_km_tro_di * (x - 21) 
        print("Cước phí là: ", cuoc_phi)


"""
Bài 4: giải phương trình bậc 2
"""
from math import sqrt

a = float(input('Nhập a: '))
b = float(input('Nhập b: '))
c = float(input('Nhập c: '))

if a == 0:
    print('Suy biến về bậc nhất')
    if b == 0:
        if c == 0:
            print('Phương trình vô số nghiệm')
        else:
            print('Phương trình vô nghiệm')
    else:
        print('phuong trinh co 1 nghiem la', -c/b)

else: # phương trình bậc 2:
    delta = (b ** 2) - (4* a* c )
    if delta > 0 :
        x1 = (-b + sqrt(delta)) /(2*a)
        x2 = (-b - sqrt(delta)) /(2*a)
        print( ' phuong trinh co 2 nghiem phan biet' , x1 ,x2 )
    else : 
        if delta == 0 :
            print(' x co nghiem kep la' , -b/ 2*a)
        else:
            print ( 'phuong trinh vo nghiem ')

"""
Nhiệm vụ về nhà
- Tự code lại tất cả các bài phía trên
- Vẽ sơ đồ khối xử lý của các bài đó
"""
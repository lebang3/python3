while True:
    n = int(input('Nhập vào số n: '))
    if n > 0:
        break

a = []
for _ in range(n):
    a.append(int(input('Nhap phan tu: ')))
print(a)

it_max = a[0]
it_min = a[0] 
count_max = 0
count_min = 0

for idx,iteam in enumerate(a):
    if it_max  < iteam :
        it_max = iteam
        count_max = idx
    if it_min > iteam:
        it_min = iteam
        count_min = idx

print("gia tri max: ",it_max," vi tri: ",count_max )
print("gia tri min: ",it_min," vi tri: ",count_min )
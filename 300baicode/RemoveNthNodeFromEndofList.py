while True:
    n = int(input(' nhap phan tu muon xoa: '))
    if n > 0:
        break

l = []

for i in range(31):
    l.append(i)
print(l)
print("----------------------------------")

l.pop(-n)

print(l)
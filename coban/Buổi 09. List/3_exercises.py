n = int(input())
l = []
a = 0

for _ in range (n):
    i = int(input("type :"))
    l.append(i)

for i in l:
    a += i

print(a)


while True:
    n = int(input('Nhập vào số n: '))
    if n > 0:
        break
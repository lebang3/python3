N = int(input('Enter an Integer:'))

s = 0
i = 1

while True:
    print('=============')
    print(i)
    if i == N + 1:
        break
    if i % 2:
        s += i
    print('s', s)
    i += 1
print(s)
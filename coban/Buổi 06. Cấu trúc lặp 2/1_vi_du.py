"""
Nhập vào N, tính tổng các số lẻ từ 1
- N sử dụng vòng lặp while
"""
N = int(input('Nhập vào N: '))

s = 0
i = 1

while i <= N:
    print('----------')
    print('i', i)
    if i % 2: # Truthy - Falsy
        # 0, '', [], {}, -> False
        # Còn lại -> coi là true
        s += i
    i += 1
    print('s', s)

print(s)

### Bài 2
epsilon = float(input('Nhập epsilon: '))

i = 0
s = 0
current = 1

while current >= epsilon:
    print('i', i)
    s += current
    i += 1
    current = current * 1/i
    print('s', s, 'current', current)

print(s)
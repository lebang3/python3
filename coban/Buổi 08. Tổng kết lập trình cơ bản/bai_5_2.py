"""
Nhập vào số nguyên dương n (giả định ng dùng luôn nhập đúng - không
cần kiểm tra) Tiếp theo, nhập n số từ bàn phím.
Hỏi:
- Tổng các số là bao nhiêu
- Tổng các số lẻ là bao nhiêu
Dành 5 phút làm 2 phần này
===========
- In ra phép tính dưới dạng tường minh: Ví dụ: 1 + 3 + 10 = 14
"""

while True:
    n = int(input('Nhập vào số n: '))
    if n > 0:
        break

s = 0
s_le = 0

s_trace = ''
s_trace_odd = ''

is_first_odd = True

for i in range(n):
    current = int(input('Nhập vào 1 số: '))
    
    s += current
    if i == 0:
        s_trace += str(current)
    else:
        s_trace += ' + ' + str(current)
    if current % 2:
        s_le += current
        if is_first_odd:
            is_first_odd = False
            s_trace_odd += str(current)
        else:
            s_trace_odd += ' + ' + str(current)
    print(s_trace_odd, s_trace, is_first_odd)

print(s_trace, '=', s)
print(s_trace_odd, '=', s_le)
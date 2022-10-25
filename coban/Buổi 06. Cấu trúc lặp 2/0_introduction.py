"""
Các vấn đề trên, đều có chung một đặc điểm, đó là không biết trước
số lần lặp như ở vòng lặp for, tuy vậy lại có thể biết được chính xác cần
dừng lại khi nào
"""

s = 0
i = 1

while i <= 5:
    print('----------')
    print('i', i)
    s += i
    i += 1
    print('s', s)

print(s)

"""
1. Tham khảo và code lại vòng lặp while
2. Code lại bằng vòng for và so sánh kết quả
"""
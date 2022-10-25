a = "abc    nbadf    def \t \n mnk abc"


"Cần in ra chuỗi được nối liền"

l = a.split()
print(''.join(l))

"""
Hai hàm bên dưới không thật sự hiệu quả trong trường hợp có các ký tự escape sequence

\t \n 
"""
print(a.strip())
print(a.replace(' ', ''))
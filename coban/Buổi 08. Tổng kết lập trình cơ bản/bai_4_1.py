"""
Bai 2:
a. Tinh S = 1 + 1/(1+2) + 1/(1+2+3) + ... + 1/(1+2+3+...+N)
b. Tinh P = 1/(1*2) + 1/(2*3) + 1/(3*4) + ... + 1/((N-1)*N)

-> Nhập 1 số N nguyên dương
-> Tính tổng S với N nhập vào
========
-> Code + in ra các biến trung gian qua các vòng lặp
"""

"""
1. Xây dựng công thức truy hồi S_i = S_(i-1) + temp
2. Xây dựng sơ đồ khối - kiểm nghiệm = tay sơ đồ khối
3. Code thử và kiểm nghiệm các biến trung gian qua từng lần lặp 
4. Nghiệm thu code so với sơ đồ khối và kết quả
"""

# n = int(input("type n = "))

# small_temp = 1
# temp = 0

# for i in range (n):
#     small_temp += i
#     temp += 1/small_temp

# print(temp)

n = int(input("Nhap so n: "))

p = 0
m = 0

for i in range(1,n+1):
    # print('-----------')
    # print(i)
    m = m + i # tổng 1-i
    p = p + 1 / m # tính current = 1/m -> cộng với result sau cùng
    # print(m, p) # in các biến trung gian
print('Result a', p)

tong = 0

for i in range(2, n+1):
    print('-------------')
    print(i)
    tong += 1/((i-1)*i)
    print(i-1, i, tong)

print("tong la:", tong)


"""
Bai 3:
In ra hinh ve
a)                              b)
***********                         *************
***********                         *           *
***********                         *           *
***********                         *************

-> Nhập vào số n, m (nguyên dương)
in ra hình chữ nhật đặc, rỗng với chiều dài m, chiều rộng n
"""
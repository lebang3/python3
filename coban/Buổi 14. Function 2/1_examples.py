def sum_of_elements(N):
    print('------------')
    print('Call sum_of_elements with N:', N)
    if N == 0:
        return 0

    # result =  N + sum_of_elements(N-1)
    # print('N:', N, ', result:', result)
    
    # return result
    return N + sum_of_elements(N-1)

while True:
    x = int(input('Nhập vào 1 số nguyên dương:'))
    if x > 0:
        break

print(sum_of_elements(x))

"""
Sử dụng đệ quy
2. Viết hàm tính n!
3. Viết hàm tính 2^n
"""

def giai_thua(n):
    if n == 0:
        return 1
    
    return giai_thua(n-1) * n
    
n = int(input("type n:"))
print(giai_thua(n))


def somu(b):
    if b == 0:
        return 1
    return 2 * somu(b - 1)

print(somu(n))
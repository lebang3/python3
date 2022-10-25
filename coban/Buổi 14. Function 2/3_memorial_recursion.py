def so_mu(n):
    print('--------------')
    print(n)
    if n == 0:
        return 1
    
    if n % 2:
        return 2 * so_mu((n-1) // 2) * so_mu((n-1) // 2)
    else:
        return so_mu(n//2) * so_mu(n//2)


"""
Lưu trữ các kết quả qua các lần đệ quy vào list/dict/...
nếu giá trị đã tính rồi -> return luôn, không tính lại
"""

x = int(input('Nhập vào 1 số nguyên: '))

memory = [-1 for _ in range(x + 1)]
## Mảng nhớ các giá trị đã tính rồi
## mặc định chưa tính -> -1
## khi tính 1 lần rồi -> update vào mảng memory
## khi gặp số tính rồi thì return luôn không cần tính lại

"""
n       :  0  1  2  3  4  5  6  7  8
value   : -1 -1 -1 -1 -1 -1 -1 -1 -1
====================================
n       :  0  1  2  3  4  5  6  7  8
value   :  1  2  4 -1 16 -1 -1 -1 -1
"""

## Còn gọi là top-down dynamic programing: Quy hoạch động top-down

def so_mu_cai_tien(n, memory):
    print('--------------')
    print(n)
    if memory[n] != -1:
        return memory[n]

    if n == 0:
        return 1
    else:
        current_result = -1
        if n % 2: # n lẻ
            current_result = 2 * so_mu_cai_tien((n-1) // 2, memory) * \
            so_mu_cai_tien((n-1) // 2, memory)
        else: # n chẵn
            current_result = so_mu_cai_tien(n//2, memory) * \
            so_mu_cai_tien(n//2, memory)

        memory[n] = current_result
        return current_result       

print(so_mu(x))
print('***********')
print(so_mu_cai_tien(x, memory))
N = 5

def fib(n):
    if n == 1:
        return 1
    
    if n == 2:
        return 1
    
    return fib(n-1) + fib(n-2)

memory = [-1 for i in range(N + 1)]

def fib_mem(n, memory, num_comp_current, num_mem_current): 
    """
    n: số fib thứ n
    memory: mảng nhớ
    -------------
    return:
        - kết quả fib
        - số lần tính
        - số lần nhớ
    """
    if memory[n] != -1:
        return memory[n], num_comp_current, num_mem_current + 1

    if n == 1 or n == 2:
        return 1, 0, 0

    result_n_minus_2, num_comp_left, num_mem_left = \
        fib_mem(n-2, memory, num_comp_current, num_mem_current)
    
    num_comp_current += 1

    result_n_minus_1, num_comp_right, num_mem_right = \
        fib_mem(n-1, memory, num_comp_current, num_mem_current)

    num_comp = num_comp_left + num_comp_right
    num_mem = num_mem_left + num_mem_right

    memory[n] = result_n_minus_1 + result_n_minus_2

    return memory[n], num_comp, num_mem

def fibo(n, mem, num_mem_current, num_compute_current):
    print(n, mem, num_mem_current, num_compute_current)
    if mem[n] != -1:
        num_mem_current += 1
        return mem[n], num_mem_current, num_compute_current

    if n == 1 or n == 2:
        return 1, 0, 0

    result2, num_mem2, num_compute2 = fibo(n-2, mem, num_mem_current, num_compute_current)
    num_compute_current += 1 # f(n-1) + f(n-2) -> tăng đếm số phép tính lên 1 đơn vị
    result1, num_mem1, num_compute1 = fibo(n-1, mem, num_mem_current, num_compute_current) 
    
    result = result1 + result2

    num_mem = num_mem1 + num_mem2
    num_compute = num_compute1 + num_compute2
    mem[n] = result

    print('*********')
    return result, num_mem, num_compute

print(fibo(N, memory, 0, 0))
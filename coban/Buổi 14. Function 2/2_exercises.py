"""
Số fibbonacci được định nghĩa là 

f(1) = 1
f(2) = 1

f(i) = f(i-1) + f(i-2) với i >= 3

Nhập vào 1 số n, tính f(n)
"""

x = int(input('Nhập vào 1 số nguyên:'))

def fibo(N):
    if N == 1 or N == 2:
        return 1
    return fibo(N - 1) + fibo(N - 2)

print(fibo(x))


import math

def s1(N):
    if N == 1:
        return 1
    return math.sqrt(N + s1(N-1))

print(s1(x))


def s2(N):
    if N == 1:
        return 1
    return 1/(1 + s2(N-1))

print(s2(x))
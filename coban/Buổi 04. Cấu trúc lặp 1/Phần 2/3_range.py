"""
- range(stop)
- range(start, stop)
"""

"""
range(stop)
-> 0...(stop-1)
"""

for i in range(10):
    print(i)

"""
range(start, stop)
-> start, start + 1, start + 2, ..., stop - 1
"""
print('-------------')
for i in range(4, 10):
    print(i)

"""
range(start, stop, step)

start, start + step, start + 2*step, ..., start + k*step, 

-> số gần nhất với stop
"""
print('-----------')
for i in range(0, 10, 3):
    print(i)
    
print('-----------')
for i in range(10, 0, -3):
    print(i)


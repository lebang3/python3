'''
Nhập vào 1 số nguyên dương n
- Khai báo list a gồm n phần tử 0, in ra a
- Khai báo list b gồm n phần tử 1 - n, in ra b
- Khai báo list c gồm n phần tử lẻ từ 1, 3, 5, ... in ra c
'''

n = int(input('n = '))

a = []

for _ in range(n):
  a.append(0)

print("a =", a)

b = []

for i in range(n):
  b.append(i + 1)

print("b =", b)

c = []
current_odd = 1

for i in range(n):
  c.append(current_odd)
  current_odd = current_odd + 2

print("c =", c)

'''
Nhập vào số nguyên dương n. Khai báo list a, nhập n phần tử vào list a.
Yêu cầu
- Khai báo list b và copy các giá trị của a vào b theo đúng thứ tự
- Khai báo list c và copy các giá trị của a vào c theo chiều đảo ngược	
'''

n = int(input('n = '))
a = []

for i in range(n):
  x = input(f'a[{i}] = ')
  a.append(int(x))

b = []

for element in a:
  b.append(element)

print('b =', b)

c = []

for i in range(n):
  c.append(a[n - i - 1])

print('c =', c)

'''
Nhập vào số nguyên dương n. Nhập vào n phần tử cho list a
Nhập vào 2 số nguyên dương a, b sao cho 0 <= a <= b < n
Hỏi: 
+ Phần tử từ ở vị trí a là gì
+ Phần tử từ vị trí a -> vị trí b là gì
+ In ra phần tử từ vị trí a -> vị trí b, mỗi 3 phần tử lấy ra và in 1 lần"
'''

n = int(input('n = '))
arr = []

for i in range(n):
  tmp = int(input(f'a[{i}] = '))
  arr.append(tmp)

a = int(input('a = '))
b = int(input('b = '))

print(f'Phần tử thứ {a}: {arr[a]}')

ab_sliced = arr[a : b + 1]
print(f'Các phần tử từ {a} đến {b}:', ab_sliced)

ab_sliced_sep = ab_sliced[ : : 3]
print("Phần tử từ vị trí a -> vị trí b, mỗi 3 phần tử lấy ra và in 1 lần:", ab_sliced_sep)

'''
Nhập vào số n, nhập vào list n phần tử số thực
+ Tổng các số trong list là bao nhiêu
+ Phần tử lớn nhất - nhỏ nhất có vị trí nào, giá trị bao nhiêu
'''
n = int(input('n = '))
arr = []
sum = 0

greatest_value_id = 0
smallest_value_id = 0

for i in range(n):
  tmp = int(input(f'a[{i}] = '))
  arr.append(tmp)

for i in range(n):
  sum = sum + arr[i]
  if i:
    if arr[i] > arr[greatest_value_id]:
      greatest_value_id = i
    if arr[i] < arr[smallest_value_id]:
      smallest_value_id = i

print("Tổng các phần tử:", sum)

print(f"Phần tử lớn nhất: arr[{greatest_value_id}] = {arr[greatest_value_id]}")
print(f"Phần tử nhỏ nhất: arr[{smallest_value_id}] = {arr[smallest_value_id]}")

'''
Nhập số n nguyên dương
- Khai báo list a rỗng
- Nhập vào từ bàn phím n số, lưu vào a
- Lặp qua các phần tử của a. In ra:
  + Số lớn nhất - vị trí của nó. Số nhỏ nhất - vị trí của nó
  + Tổng - tích các phần tử
  + Chạy bằng tay từng dòng code theo dữ liệu nhập vào. Thêm print để kiểm nghiệm kết quả.
'''

a = []

elements_sum = 0
elements_product = 1

max_element = 0
max_element_id = 0

min_element = 0
min_element_id = 0

n = int(input('n = '))

for i in range(n):
  print('a[', i, '] = ', sep='', end='')
  element = int(input())
  a.append(element)

  if i:
    if a[i] > max_element:
      max_element = a[i]
      max_element_id = i 
    if a[i] < min_element:
      min_element = a[i]
      min_element_id = i 
  else:
    max_element = a[i]
    max_element_id = i 
    min_element = a[i]
    min_element_id = i 

  elements_sum = elements_sum + a[i]
  elements_product = elements_product * a[i]

  print("Phần tử nhỏ nhất:", min_element, 'ở vị trí', min_element_id)
  print("Phần tử lớn nhất:", min_element, 'ở vị trí', min_element_id)

  print("Tổng các phần tử:", elements_sum)
  print("Tích các phần tử:", elements_product) 

'''
Viết chương trình
- Nhập vào mảng các số nguyên, có số phần tử n  
- In ra tất cả vị trí của các phần tử trong mảng có giá trị x, với x được nhập vào từ bàn phím. Nếu không có, in ra -1 
- Nếu có từ 2 vị trí trở lên, in ra vị trí đầu tiên từ trái sang phải của phần tử có giá trị x. Nếu không có, in ra -1. 
 ương tự với phần tử tính từ phải sang trái 
- Tìm phần tử chẵn cuối cùng trong mảng, nếu không có , in ra -1 
'''

n = int(input('n = '))
a = []

for i in range(n):
  print('a[', i, '] = ', sep='', end='')
  element = int(input())
  a.append(element)

x = int(input('x = '))
position_x = [] 

for i in range(n):
  if a[i] == x:
    position_x.append(i)

if position_x:
  print('Các vị trí của', x, 'là:', end=' ')
  for pos in position_x:
    print(pos, end=' ')
  if len(position_x) >= 2:
    print('')
    print('Các vị trí đầu tiên xuất hiện', x, 'là:', position_x[0])
    print('Các vị trí cuối cùng xuất hiện', x, 'là:', position_x[-1])
else:
  print(-1)

last_even_element = -1

for element in a:
  if element % 2 == 0:
    last_even_element = element

if last_even_element >= 0:
  print('Phần tử chẵn cuối:', last_even_element)
else:
  print(last_even_element) 

'''
Viết chương trình 
- Đếm số phần tử chẵn trong mảng n phần tử nguyên được nhập vào từ bàn phím 
- Đếm số phần tử chính phương trong mảng trên 
- Đếm số phần tử có giá trị x, với x nhập vào từ bàn phím 
- Đếm số phần tử có giá trị <= x 
'''

import math

n = int(input('n = '))
a = []

n_evens = 0
n_perfect_sqrt = 0

for i in range(n):
  print('a[', i, '] = ', sep='', end='')
  element = int(input())
  a.append(element)

for i in a:
  if i % 2 == 0:
    n_evens += 1
  sqrt_i = int(math.sqrt(i))
  
  if i == sqrt_i * sqrt_i:
    n_perfect_sqrt += 1

print("Số phần tử chẵn trong mảng:", n_evens)
print("Số các số chính phương trong mảng:", n_perfect_sqrt)

x = int(input('x = '))

n_equal_x = 0
n_leq_x = 0

for i in a:
  if i <= x:
    n_leq_x += 1
  if i == x:
    n_equal_x += 1

print("Số phần tử bằng ", x, ': ', n_equal_x, sep='')
print("Số phần tử <= ", x, ': ', n_leq_x, sep='')


'''
Viết chương trình 
- Nhập hai số nguyên dương m, n
- Nhập vào một ma trận các số thực kích thước m x n
- In ra ma trận đó 
'''
m = int(input('m = '))
n = int(input('n = '))

mat = []

for i in range(m):
  temp_row = []
  for j in range(n):
    print(f'a[{i}][{j}] = ', end='')
    current_cell = int(input())
    temp_row.append(current_cell)
  mat.append(temp_row)

for row in mat:
  for cell in row:
    print(cell, end='\t')
  print('')
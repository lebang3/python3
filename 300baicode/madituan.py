m = int(input('m = '))
n = int(input('n = '))

mat = []

for i in range(m):
  temp_row = []  # tao mot list rong 
  for j in range(n): 
    print(f'a[{i}][{j}] = ', end='') # gan end = ""
    current_cell = int(input())
    temp_row.append(current_cell) # va dong tren de gan phan tu vao temp_row
  mat.append(temp_row) # ga lai

for row in mat:
  for cell in row:
    print(cell, end='\t')
  print('')
  
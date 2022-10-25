"""
Viết chương trình
a. Khởi tạo một dictionary, có key là 'a' - 'z', value đều là 0. In ra dict đó
b. Nhập vào một chuỗi họ  tên không dấu, in ra chuỗi đó
c. In ra mỗi kí tự đã xuất hiện bao nhiêu lần sử dụng dict đã khai báo ở câu a
"""

char_dict = {}

a_ascii_pos = ord('a')

for i in range(26):
  char_dict[chr(a_ascii_pos + i)] = 0

print(char_dict)

name = input("Nhập tên không dấu: ")
print(f"Tên vừa nhập: {name}")

name = name.lower()

for char in name:
  if char != ' ':
    char_dict[char] += 1

for char, freq in char_dict.items():
  if freq:
    print(f'{char}: {freq}')

""" 
Viết chương trình
a. Khai báo một dict có key là chữ, value là số nguyên không âm
b. Đảo ngược key và value. In ra dict mới có dạng value:key
Nếu không thể nghịch đảo, in ra -1
"""
char_dict = {}

reversed_dict = {}

for i in range(ord('a'), ord('z') + 1):
  char_dict[chr(i)] = int(input(f"{chr(i)}: "))

has_dup_val = False

dict_vals = []

for val in list(char_dict.values()):
  if val not in dict_vals:
    dict_vals.append(val)
  else:
    has_dup_val = True
    break

if has_dup_val:
  print(-1)
else:
  for (key, value) in char_dict.items():
    reversed_dict[value] = key

  print('Dict mới')
  for (key, value) in reversed_dict.items():
    print(f'{value}: {key}')

'''
Hỏi người dùng có muốn nhập tiếp không (y/n). Nếu n, kết thúc chương trình 
Nếu y, nhập vào key - value cho dictionary  
Nếu 
- Key đã tồn tại - in ra theo mẫu: Update giá trị cho {key} từ {old} sang {new} 
- Key chưa có - in ra theo mẫu: Thêm mới {key} - {val} 
'''

answer = input("Có muốn nhập tiếp (y/n): ")

user_dict = {}

while answer == 'y':
  key = input('Nhập key: ')
  val = input('Nhập value: ')

  if key in user_dict:
    print(f"Update giá trị cho {key} từ {user_dict[key]} sang {val}")
  else:
    print(f"Thêm mới {key} - {val} ")
    
  user_dict[key] = val

  answer = input("Có muốn nhập tiếp (y/n): ")

"""
Viết chương trình 
Nhập vào 1 dictionary có value là các phần tử số nguyên 
Tính tích các value là số lẻ 
"""
n = int(input("n = "))

num_dict = {}

odd_prod = 1

for i in range(n):
  key = input('Nhập key: ')
  val = int(input('Nhập value: '))

  num_dict[key] = val

for value in list(num_dict.values()):
  if value % 2:
    odd_prod *= value

print(f"Tích các value là số lẻ: {odd_prod}")

""" 
Viết chương trình tạo dict mới bằng cách trích xuất dữ liệu từ dict ban đầu 
theo tập các key cho trước 
Ví dụ: 
sampleDict = {""name"": ""Kelly"", ""age"":25, ""salary"": 8000, ""city"": ""New york""} 
keys = [""name"", ""salary""] 
Output: {'name': 'Kelly', 'salary': 8000} 
"""
sample_dict = {
  "name": "Kelly", 
  "age": 25, 
  "salary": 8000, 
  "city": "New york"
} 

keys = ["name", "salary"] 

output_dict = {}

for key in keys:
  if key in sample_dict:
    output_dict[key] = sample_dict[key]

print(output_dict)

# Viết chương trình lấy ra các cặp key - value xuất hiện chung trong 2 dictionary được nhập từ bàn phím 
dict_1 = {}
dict_2 = {}

common_pairs = {}

n = int(input("n = "))

print('Dictionary 1')
for i in range(n):
  key = input('Nhập key: ')
  val = int(input('Nhập value: '))

  dict_1[key] = val

print('Dictionary 2')
for i in range(n):
  key = input('Nhập key: ')
  val = int(input('Nhập value: '))

  dict_2[key] = val

for key in list(dict_1.keys()):
  if key in dict_2 and dict_1[key] == dict_2[key]:
    common_pairs[key] = dict_1[key]

print("Các cặp key-value chung:", common_pairs)
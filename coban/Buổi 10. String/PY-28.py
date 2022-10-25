# In ra các ký tự ascii của một string dưới dạng list
s = input("Nhập chuỗi: ")

char_arr = []

for ch in s:
  char_arr.append(ch)

print(char_arr)

'''
Nhập vào duy nhất 1 ký tự chữ cái 
- Nếu sai, yêu cầu nhập lại 
- Nếu là ký tự thường, đổi thành chữ hoa rổi in ra
- Nếu là kí tự hoa, in ra luôn kết quả
'''
char = input("Nhập 1 kí tự chữ cái: ")
while len(char) != 1 or char < 'A' or 'Z' < char < 'a' or char >= 'z':
  print("Nhập lại!")
  char = input("Nhập 1 kí tự chữ cái: ")

if char >= 'a':
  char = chr(ord(char) - ord('a') + ord('A'))

print(char)

# Cho 1 string với rất nhiều dấu space thừa. sử dụng split, join để xóa các space thừa

inp_str = input("Nhập chuỗi: ")

char_arr = inp_str.split()

striped_str = " ".join(char_arr) #chuyen list thanh str cach nhau mot dau ' '

print("Chuỗi xoá khoảng trống:", striped_str)

'''
Nhập vào 1 string có ít nhất 3 ký tự.
- Thay 1 ký tự đầu tiên bằng 'H'. In ra kết quả, id trong ascii của kết quả
- Thay 2 ký tự đầu tiên bằng 'He'. In ra kết quả, id trong ascii của kết quả
'''
input_str = input("Nhập chuỗi: ")

replaced_str_1 = f"H{input_str[ 1 : : ]}"

print(f"Chuỗi sau khi thay 1 kí tự đầu bằng 'H': {replaced_str_1}")
print(f"Mã ascii chuỗi sau khi thay 1 kí tự đầu bằng 'H': ", end='')

for c in replaced_str_1:
  print(ord(c), end=' ')

print('')

replaced_str_2 = f"He{input_str[ 2 : : ]}"

print(f"Chuỗi sau khi thay 2 kí tự đầu bằng 'He': {replaced_str_2}")
print(f"Mã ascii chuỗi sau khi thay 2 kí tự đầu bằng 'He': ", end='')

for c in replaced_str_2:
  print(ord(c), end=' ')

print('')

# Build chức năng tìm kiếm chuỗi
'''
Nhập vào 1 chuỗi kí tự tiếng anh, lưu ở biến s. Nhập vào kí tự c
- Đếm số lần xuất hiện của các kí tự trong s
- Tìm kiếm tất cả vị trí kí tự c  trong chuỗi. Nếu không tìm thấy in ra -1
- Tìm kiếm vị trí đầu tiên xuất hiện kí tự c từ trái sang phải, từ phải sang trái, nếu không tìm thấy in ra -1
'''
s = input("Nhập chuỗi: ")
c = input("Nhập 1 kí tự: ")

emergence_pos = []

for i in range(len(s)):
  if c == s[i]:
    emergence_pos.append(i)

print(f"Số lần kí tự '{c}' xuất hiện trong xâu:", len(emergence_pos))

if emergence_pos:
  print(f"Các vị trí xuất hiện '{c}': {emergence_pos}")
  print(f"Các vị trí đầu tiên xuất hiện '{c}' từ trái sang phải: {emergence_pos[0]}")
  print(f"Các vị trí đầu tiên xuất hiện '{c}' từ phải sang trái: {emergence_pos[-1]}")

else:
  print(f"Các vị trí xuất hiện '{c}': -1")
  print(f"Các vị trí đầu tiên xuất hiện '{c}' từ trái sang phải: -1")
  print(f"Các vị trí đầu tiên xuất hiện '{c}' từ phải sang trái: -1")

# Xử lý chuỗi 
'''
Nhập vào 1 chuỗi kí tự, lưu ở biến s
Đổi các chữ cái về in thường, loại bỏ các kí tự không phải số và không phải chữ, in ra chuỗi kí tự đã xử lý"
'''

s = input("Nhập chuỗi: ")

processed_str = ''

for char in s:
  if 'A' <= char <= 'Z':
    char = chr(ord(char) + ord('a'))

  if 'a' <= char <= 'z' or '0' <= char <= '9':
    processed_str = processed_str + char

print("Chuỗi đã xử lý:", processed_str)

# Xử lý chuỗi nâng cao
'''
Nhập vào tên người. VD quaCh hUy TunG
Chuẩn hóa về dạng chuẩn Quach Huy Tung (chữ đầu mỗi từ viết hoa)
'''
lower_upper_diff = ord('a') - ord('A')

s = input("Nhập tên người: ")

proper_name = ''

for i in range(len(s)):
  if (i == 0 or s[i - 1] == ' ') and 'a' <= s[i] <= 'z':
    upper_char = chr(ord(s[i]) - lower_upper_diff)
    proper_name = f"{proper_name}{upper_char}"
  elif 'A' <= s[i] <= 'Z':
    lower_char = chr(ord(s[i]) + lower_upper_diff)
    proper_name = f"{proper_name}{lower_char}"
  else:
    proper_name = f"{proper_name}{s[i]}"

print("Tên sau khi chuẩn hoá:", proper_name)

'''
Bài tập về nhà
1. Viết chương trình:
- Nhập vào 1 chuỗi kí tự, lưu ở biến s
- In ra chuỗi kí tự đó theo cú pháp: Your input string is: ""...""
- In ra giá trị mã ASCII của chuỗi kí tự đó trên cùng 1 dòng
- Đổi các chữ cái về in thường, loại bỏ các kí tự không phải số hoặc chữ, in ra chuỗi kí tự đã xử lý
- Xóa bỏ tất cả các khoảng trắng
- In hoa chữ cái đầu chuỗi hoặc sau khoảng trắng như viết tên người
'''
s = input("Nhập chuỗi: ")

print(f"Your input string is: {s}, mã ascii: ", end='')

for ch in s:
  print(ord(ch), end=' ')

print('')

alpha_nums_str = ''

for ch in s:
  # if isalnum(ch):
  if 'a' <= ch <= 'z' or 'A' <= ch <= 'Z' or '0' <= ch <= '9':
    alpha_nums_str = f"{alpha_nums_str}{ch}"

print(f"Chuỗi chỉ gồm chữ cái và số: {alpha_nums_str}")

trimmed_str = ''.join(s.split(" "))

'''
2. Viết chương trình:
- Nhập vào 1 chuỗi s, 1 số d. Dịch chuỗi s đi 1 khoảng d trên bảng mã ascii thu được s'. In ra s'
- Nhận xét kết quả nếu có chữ z trong chuỗi s
'''
s = input('s = ')
d = int(input('d = '))

s_trans = ""

for ch in s:
  s_trans = f"{s_trans}{chr(ord(ch) + d)}"

print(f"Chuỗi đã dịch: {s_trans}")

'''
3. Mật mã Caesar là một bộ mã hóa như sau:
- Một kí tự được dịch đi một khoảng cách d là một số nguyên (0 < d < 26)
- Nếu việc dịch đó làm kí tự ra ngoài khoảng cho phép, quay vòng về ‘a', ‘A' rồi tiếp tục dịch
Ví dụ: với d = 2, a -> c, m -> k, z -> b
Viết chương trình:
Cho người dùng lựa chọn chế độ:
- 0. thoát chương trình
- 1. mã hóa 
- 2 giải mã
Với chế độ 1, 2
- Nhập vào khoảng cách d
- Nhập vào một chuối kí tự s
- Đưa ra kết quả tương ứng
Lưu ý: phân biệt hoa - thường
'''

mode = 0

while True:
  print("""
Chọn chế độ:
- 0. thoát chương trình
- 1. mã hóa 
- 2 giải mã
  """)  
  option = int(input('Lựa chọn: '))

  if 0 <= option < 3:
    break

if option:
  d = int(input('Khoảng cách: d = '))

  while d <= 0 or d >= 26:
    print('0 < d < 26')
    d = int(input('Khoảng cách: d = '))

  s = input('Nhập chuỗi: ')

  result_str = ''

  for ch in s:

    start_char_pos = ord('a') if ch >= 'a' else ord('A')
    end_char_pos = ord('z') if ch >= 'a' else ord('Z')

    if option == 1:
      pos = ord(ch) + d
      if pos > end_char_pos:
        pos = pos - 26
    else:
      pos = ord(ch) - d
      if pos < start_char_pos:
        pos = pos + 26

    new_char = chr(pos)

    result_str += new_char
  
  if option == 1:
    print('Chuỗi mã hoá:', end=' ')
  else:
    print('Chuỗi giải mã:', end=' ')

  print(result_str)

'''
4. Nhập 1 chuỗi s, yêu cầu chỉ có các ký tự chữ cái. Chuẩn hóa toàn bộ s về chữ cái thường
Hỏi có bao nhiêu chữ cái xuất hiện trong s, mỗi chữ cái xuất hiện bao nhiêu lần?
'''
s = input("s = ")

s = s.lower()

table = [0 for _ in range(26)]

distinct_char = 0

for char in s: 
  simplified_id = ord(char) - ord('a')
  if table[simplified_id] == 0:
    distinct_char += 1
  table[simplified_id] += 1

print(f"Số chữ cái: {distinct_char}")

for i in range(len(table)):
  if table[i]:
    print(f"{chr(ord('a') + i)}: {table[i]}")
"""
String: chuỗi ký tự (a-z, A-Z, 0-9, !, #, ...)

String có thể mở rộng ra các ký tự đặc biệt ă, â, ơ, kí tự tiếng trung, hàn, nhật, ... (unicode)
"""

a = 'abc'
b = "def"

c = """
hello
12345
$#$%$@Q@!#
"""

print(a, type(a))
print(b, type(b))
print(c, type(c))

print('a', ord('a')) # từ chữ -> số trên bảng mã ascii
print(68, chr(68)) # từ số -> chữ trên bảng mã ascii

s = "abcdef"

for i in range(len(s)):
    print(i, s[i])
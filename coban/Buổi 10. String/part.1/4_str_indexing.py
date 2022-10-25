l = [1, 2, 3, 'mnk', 1.2, 3.0]

print(l)
l[2] = 300
print(l)

"""
String là một immutable data type điển hình
khi tạo ra rồi 
không gán lại được nữa

s = 'mnkabcdef'
s[3] = '2'
"""

a = "congacon"
print(a, id(a))
s1 = 'H' + a[1:]
print(s1, id(s1))
s2 = 'He' + a[2:]
print(s2, id(s2))
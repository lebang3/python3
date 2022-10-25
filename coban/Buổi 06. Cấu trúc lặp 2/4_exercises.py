"""
Nhập vào 1 ký tự
"""
s1 = ''
while True:
    s = input('Nhập vào 1 ký tự:')
    
    if len(s) == 1:
        break
    s1 += ' ' + s
    print(s, 'không hợp lệ')

print('Ký tự nhập vào hợp lệ', s)
print('Ký tự nhập vào không hợp lệ', s1)


"""
Nhập vào 1 ký tự
"""
s2 = ''
while True:
    s = input('Nhập vào 1 ký tự:')
    
    if len(s) == 1 and '0' <= s <= '9':
        break
    s2 += ' ' + s
    print(s, 'không hợp lệ')

print('Ký tự nhập vào', s)
print('Ký tự nhập vào không hợp lệ', s2)

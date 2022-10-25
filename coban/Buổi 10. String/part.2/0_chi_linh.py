s = str(input('Nhap vao chuoi ki tu: '))
b = []

for c in s:
    if 'A' <= c <= 'Z':
        b.append(chr(ord(c) + 32))
    else:
        b.append(c)

standard_string = "".join(b)
print(standard_string)

result = ''

for d in standard_string.split():
    result += chr(ord(d[0]) - 32) + d[1:] + ' '

print(result)
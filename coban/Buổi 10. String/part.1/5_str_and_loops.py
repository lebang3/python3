s = 'ad123'

## C1 lap bang chi so
print(id(s), len(s))

for i in range(len(s)):
    print(i, s[i])

# c2 Lap bang cac phan tu
for c in s:
    print(c)

# c3 lap bang ca phan tu va chi so
for i, c in enumerate(s):
    print(i, c)
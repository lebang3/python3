l = [x for x in range(1, 10)]

for i in map(lambda x: x + 2, l):
    print(i)
    
print(list(map(lambda x: x + 2, l)))
print(list(filter(lambda x: x % 2, l)))

l1 = [x for x in l if x % 2]
print(l1)


l2 = []

for item in l:
    if item % 2:
        l2.append(item)

print(l2)
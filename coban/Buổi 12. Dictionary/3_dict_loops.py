d3 = {
    'a': 1,
    'b': 2,
    'a': 5,
    1: 'a',
    2.2: 1,
    ('a', 'b'): ['a', 1]
}

for k in d3.keys(): # key - dict = index - list
    print(k, d3[k])
print('-------------')
for v in d3.values():
    print(v)
print('-------------')
for k, v in d3.items():
    print(k, v)
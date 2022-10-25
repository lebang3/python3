d3 = {
    'a': 1,
    'b': 2,
    'a': 5,
    1: 'a',
    2.2: 1,
    ('a', 'b'): ['a', 1]
}

# Add key-value
d3['c'] = 1000
print(d3)

# update element
d3['c'] = 10
print(d3)

# delete element
del d3['c']
print(d3)

val = d3.pop('a')
print(val, d3)

## others
print(len(d3))
print(d3.items())
print(d3.keys())
print(d3.values())

del d3
# print(d3)
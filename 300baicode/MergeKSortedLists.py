l = [[1,4,5],[1,3,4],[2,6]]
h = []
k = []


for i in range(len(l)):
    h = l[i]
    print(h)
    for j in range(len(h)):
        k.append(h[j])
    h.clear()
k.sort()
print(k)


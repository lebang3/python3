l= [0,1,2,3,4,5,6,7,8,9,10]
l_1 =[]

# while True:

#     ch = int(input("1: nhap them bien vao list,0: de dung: "))
#     if ch == 1 :
#         n = int(input("nhap phan tu: "))
#         l.append(n)
#     else:
#         break
# print(l)

taget = int(input("nhap taget: "))
s = ""
for idx_1, item_1 in enumerate(l) :
    if idx_1 <= (len(l)//2):
        for idx_2 , item_2 in enumerate(l):
            if item_1 + item_2 == taget and idx_1 != idx_2:
                s = str(idx_1) + ","+ str(idx_2)

                l_1.append(s)
                s = ""
    else:
        break

print(l_1)

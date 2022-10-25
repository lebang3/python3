while True:
    s = input ("nhap chuoi: ")
    if  1 <= len(s) and len(s) <= 15 :
        break
s=s.upper()
print(s)
l = ""
number = 0
for idx, c in enumerate(s):
    if c != " " : 
        l = l + c + " "
    else:
        l = l + c 
print(l,type(l))
from tkinter import N


number = int(input("so can chuyen doi: "))
l = []
for i in range(4):
    n = number % 10
    l.insert(0,n)
    number = number // 10
roman = "" 
#nghin

roman = roman + ("M" * l[0])
#tram
if l[1] == 9 :
    roman = roman + "CM"
    print("cm")
elif 9>=l[1] >= 5:
    roman = roman + "D" + "C" * (l[1]-5)
    print("dc")
if l[1] == 4 :
    roman = roman + "CD"
    print("cd")
elif l[1] < 5:
    roman = roman + "C" * l[1]
    print("c")
# chuc
if l[2] == 9 :
    roman = roman + "XC"
    print("xc")
elif 9>=l[2] >= 5:
    roman = roman + "L" + "X" * (l[2]-5)
    print("lx")
if l[2] == 4 :
    roman = roman + "XL"
    print("xl")
elif l[2] < 5:
    roman = roman + "X" * l[2]
    print("x")
#Don vi
if l[3] == 9 :
    roman = roman + "IX"
elif 9>=l[3] >= 5:
    roman = roman + "V" + "I" * (l[3]-5)
if l[3] == 4 :
    roman = roman + "IV"
elif l[3] < 5:
    roman = roman + "I" * l[3]

print(roman)
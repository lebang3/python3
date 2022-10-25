def lama(l):
    number = 0 
    for idx, c in enumerate(s):
        if c != " " : 
            l = l + c + " "
        else:
            l = l + c 
    l = l.split(" ")
    if l[0] == "M" and l[-1] == "C": #truong hop dau la M ket thuc la C
        for  idx, item in enumerate(l):
            if item == "M":
                number = number +1000
                print("M ", number)
            elif item == "D":
                if l[idx-1] == "C":
                    continue
                else:
                    number = number + 500
                    print("D ", number)
            elif item == "C":
                if l[idx+1] == "M":
                    number = number + 900
                    print("CM ", number)
                elif l[idx+1] == "D":
                    number = number + 400
                    print("CD ", number)
                else:
                    number = number + 100
                    print("C ", number)


    else:        
        for idx, item in enumerate(l):
            #don gian dai dong
            # nghin tram
            if item == "M":
                if l[idx-1] == "C":
                    continue
                else:
                    number = number + 1000
                    print("M ", number)
            elif item == "D":
                if l[idx-1] == "C":
                    continue
                else:
                    number = number + 500
                    print("D ", number)
            elif item == "C":
                if l[idx-1] == "X":
                    continue
                elif l[idx+1] == "M":
                    number = number + 900
                    print("CM ", number)
                elif l[idx+1] == "D":
                    number = number + 400
                    print("CD ", number)
                else:
                    number = number + 100
                    print("C ", number)

            #chuc
            elif item == "L":
                if l[idx-1] == "X":
                    continue
                else:
                    number = number + 50
                    print("L ", number)
            elif item == "X":
                if l[idx+1] == "C":
                    number = number + 90
                    print("XC ", number)
                elif l[idx+1] == "L":
                    number = number + 40
                    print("XL ", number)
                else:
                    number = number + 10
                    print("X ", number)
            #don vi
            elif item == "V":
                if l[idx-1] == "I":
                    continue
                else:
                    number = number + 5
                    print("V ", number)
            elif item == "I":
                if l[idx+1] == "X":
                    number = number + 9
                    print("IX ", number)
                elif l[idx+1] == "V":
                    number = number + 4
                    print("IV ", number)
                else:
                    number = number + 1
                    print("I ", number)
            
    return number


while True:
    s = input ("nhap chuoi: ")
    if  1 <= len(s) and len(s) <= 15 :
        break
s=s.upper()
print(s)
l = ""
print(lama(l))

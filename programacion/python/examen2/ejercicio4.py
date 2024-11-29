txt=""
mi=int(input("dame un numero "))
ma=int(input("dame otro "))
inte=int(input("dame uno mas "))
txt=str(mi)
for contado in range(mi+inte,ma+1,inte):
    txt=txt+","+str(contado)
txt=txt
print(txt)
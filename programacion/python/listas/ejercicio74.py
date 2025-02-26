lis1=["casa","mesa","sal","sol","agua"]
lis2=["casa","luz","tres","tren","sol","pan"]
rep=[]
no=[]
for reco in lis2:
    if reco in lis1:
        rep.append(reco)
    else:
        no.append(reco)
for reco in lis1:
    if reco in lis2:
        rep.append(reco)
    else:
        no.append(reco)    
rep=set(rep)
no=set(no)

print("se repiten: ", rep)
print("no se repiten: ", no)
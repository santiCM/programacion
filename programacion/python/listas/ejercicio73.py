lis1=["casa","mesa","sal","sol","agua"]
lis2=["casa","luz","tres","tren","sol","pan"]
rep=[]
no=[]
for reco in lis2:
    if reco in lis1:
        rep.append(reco)
    else:
        no.append(reco)
print("se repiten: ", rep)
print("no se repiten: ", no)
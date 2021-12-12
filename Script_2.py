import pandas as pd
rowf,rowg,rowh,finalrows=[],[],[],[]
testf,testg,testh=True,True,True

with open("final.csv") as  f : #Renewable Dataset
    for a in f :
        af=a.split(",")
        if testf :
            testf=False
            colf=af
            continue
        rowf.append(af)
        
for i in rowf :
    i[4]=i[4].rstrip("\n")

with open("Index_History_Clean.csv") as g : #Indexes Dataset
    for b in g :
        ag=b.split(",")
        if testg :
            testg=False
            ag[0]="Year"
            ag[12]=ag[12].rstrip("\n")
            colg=ag
            continue
        rowg.append(ag[0:13])



for i in rowg :
    i[12]=i[12].rstrip("\n")   
    for j in rowf :
        if i[0]==j[0] :
            finalrows.append(i+j[1:])



with open("Companies_all_together.csv") as h : #Companies Dataset
    for c in h :
        ah=c.split(",")
        if testh :
            testh=False
            colh=ah
            
            continue
        rowh.append(ah)

finale=[]
for i in finalrows :
    for j in rowh :
        if j[0][3:]==i[1][3:] :
            finale.append(i+j[1:])

finalcols=colg+colf[1:]+colh[1:]
finalcols[16]=finalcols[16].rstrip("\n")
finalcols[26]=finalcols[26].rstrip("\n")
               
for i in range(len(finale)) :
    finale[i]=finale[i][0:27]
    finale[i][26]=finale[i][26].rstrip("\n")
    print(finale[i])
    
integrated=pd.DataFrame(finale,columns=finalcols)
integrated.to_csv('integrated.csv',index=False)

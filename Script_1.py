import pandas as pd
ok=False
test=True
count=1
skipr,skipc=[],[]
w,col=[],[]
for i in range(1960,2005):
    skipc.append(str(i))
for i in range(2016,2021):
    skipc.append(str(i))
    
with open("Clean Data.csv") as f :
    for row in f :
        a=row.split(",")

        for i in range(len(a)) :
            a[i]=a[i].strip('"')
            if a[i]=='' :
                a[i]=0
                
        clean=[a[2]]+a[44:60]
        
        if test :
            test=False
            col=clean
            
        
        if a[3] in ['EG.FEC.RNEW.ZS','EG.ELC.RNWX.ZS','EG.ELC.RNWX.KH','EG.ELC.RNEW.ZS']:
            if a[1]=='USA' :
                ok=True
                w.append(clean)
                
        if ok==False :
            skipr.append(count)
        count+=1
        ok=False

final=pd.DataFrame(w,columns=col)
final.to_csv('final',index=False)

#Transposing the Data

d,r=[],[]
with open("final.csv") as f :
    for row in f :
        a=row.split(",")
        d.append(a)

for i in range(len(d[0])) :
    v=[]
    for k in d :
        v.append(k[i])
    r.append(v)

for i in range(5):
    r[16][i]=r[16][i].rstrip("\n")
r[0][0]="Year"
final=pd.DataFrame(r[1:],columns=r[0])
final.to_csv('final.csv',index=False)

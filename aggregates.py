#Aggregate-1

test=True
c=8.205996942 #The production value for 2000
b=0
rise,drop=0,0
ryear,dyear=0,0
with open("final.csv") as f :
    for row in f :
        a=row.split(",")
        if test :
            test=False
            continue
        b=a[4].rstrip("\n")
        diff=float(b)-float(c)
        if diff> rise :
            rise=diff
            ryear=float(a[0])
        elif diff<drop :
            drop=diff
            dyear=float(a[0])
        else :
            pass
        c=b

    print("The biggest rise in production was between {} and {}".format(ryear-1,ryear))
    print("The biggest drop in production was between {} and {}".format(dyear-1,dyear))

m1,m2,m3,m4=0,0,0,0
with open("final.csv") as f :
    for row in f :
        a=row.split(",")
        if test :
            test=False
            continue
        a[4]=a[4].rstrip("\n")
        for i in a :
            if i[1]>m1 :
                m1=i[1]
            elif
final.csv") as f :
    rem=[]
    for row in f :
        a=row.split(",")
        if test :
            test=False
            continue
        for i in a :
            if i=='' :
                rem.append(a)


#Grouped Aggregate

test=True
s1,s2,s3=0,0,0

with open("final.csv") as f :
    for row in f :
        a=row.split(",")
        if test :
            test=False
            continue
        if int(a[0]) in range(2000,2006):
            s1+=float(a[4])
        elif int(a[0]) in range(2006,2011):
            s2+=float(a[4])
        elif int(a[0]) in range(2010,2016):
            s3+=float(a[4])
        else :
            pass
        
print("For the period 2000-2005, the Average Renewable Electricity output was {}%".format(round(s1/6,2)))
print("For the period 2006-2010, the Average Renewable Electricity output was {}%".format(round(s2/5,2)))
print("For the period 2011-2015, the Average Renewable Electricity output was {}%".format(round(s3/5,2)))

#Aggregate-2

test=True
div={}

with open("final.csv") as f :
    for row in f :
        a=row.split(",")
        if test :
            test=False
            continue
        div[float(a[1])/float(a[4])]=a[0]
        
req=max(div.keys())

print("The Highest Percentage of Renewable Energy consumption to production is {}% in {}".format(req*100,div[req]))    


#Quality Check-1

test=True
with open("final.csv") as f :
    for row in f :
        a=row.split(",")
        a[4]=a[4].rstrip("\n")
        if test :
            test=False
            continue
        if (float(a[1])>0) and (float(a[2])>0) and (float(a[4])>0) :
            if (float(a[1])<=100) and (float(a[2])<=100) and (float(a[4])<=100) :
                pass
            else :
                raise ValueError
        else :
            raise ValueError

#Quality Check-2
test=True
with open("final.csv") as f :
    for row in f :
        a=row.split(",")
        a[4]=a[4].rstrip("\n")
        if test :
            test=False
            continue
        for i in a :
            if a=='' :
                raise ValueError



#Quality Check-3
test=True
with open("final.csv") as f :
    for row in f :
        a=row.split(",")
        a[4]=a[4].rstrip("\n")
        if test :
            test=False
            for i in a :
                if type(i)==str :
                    pass
                else :
                    raise TypeError
            continue
        for i in a :
            try :
                r=float(i)
            except :
                raise ValueError

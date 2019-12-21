import pandas as pd
d=pd.read_csv("dataset.csv")
f=sum(list(d["K_A_Female_Total"]))
m=sum(list(d["K_A_Male_Total"]))
import matplotlib.pyplot as plt
import seaborn as sns
plt.figure(figsize=(7,7))
plt.pie([f,m],shadow=True,explode=(0.3,0),labels=["Female ratio","Male ratio"],autopct="%1.1f%%")
plt.title("RATIO OF MALE AND FEMALE VICTIMS")
plt.show()
f10=sum(list(d["K_A_Female_Upto_10_Years"]))
f15=sum(list(d["K_A_Female_10_15_Years"]))
f18=sum(list(d["K_A_Female_15_18_Years"]))
f30=sum(list(d["K_A_Female_18_30_Years"]))
f50=sum(list(d["K_A_Female_30_50_Years"]))
fa50=sum(list(d["K_A_Female_Above_50_Years"]))
m10=sum(list(d["K_A_Male_Upto_10_Years"]))
m15=sum(list(d["K_A_Male_10_15_Years"]))
m18=sum(list(d["K_A_Male_15_18_Years"]))
m30=sum(list(d["K_A_Male_18_30_Years"]))
m50=sum(list(d["K_A_Male_30_50_Years"]))
ma50=sum(list(d["K_A_Male_Above_50_Years"]))
yt=list(d["Year"])
ca=list(d["K_A_Cases_Reported"])
k=0
l=[]
for i in range(len(yt)-1):
    if(yt[i]!=yt[i+1]):
        l.append(k)
        k=0
        z=i
    k+=ca[i]
l.append(sum(ca[z:len(yt)+1]))
cases=l
n1=[]
for i in range(len(yt)):
    if(yt[i] not in n1):
        n1.append(yt[i])
years=n1
gn=list(d["Group_Name"])
o=[]
for i in gn :
    if i not in o:
        o.append(i)
ka=list(d["K_A_Cases_Reported"])
jo=[]
for i in range(len(ka)):
    jo.append([gn[i],ka[i]])
su=0
w=[]
for i in range(len(o)):
    su=0
    for j in range(len(jo)):
        if(jo[j][0]==o[i]):
            su+=jo[j][1]
    w.append(su)
plt.figure(figsize=(7,7))
sn=list(d["Area_Name"])
du=[]
for i in range(len(sn)):
    if(sn[i] not in du):
        du.append(sn[i])
co=[]
for i in range(len(sn)):
    co.append([sn[i],ka[i]])
re=[]
for i in range(len(du)):
    ad=0
    for j in range(len(co)):
        if(co[j][0]==du[i]):
            ad+=co[j][1]
    re.append(ad)
plt.title("AGE DISTRIBUTION OF FEMALE VICTIMS OF KIDNAPP")
x=plt.pie([f10,f15,f18,f30,f50,fa50],labels=["fm(<10years)]","fm(10-15 years)","fm(15-18 years)","fm(18-30 years)","fm(30-50 years)","fm(>50years)"],autopct="%1.1f%%",shadow=True,explode=(0.1,0.1,0.1,0.1,0.1,0.1))
plt.show()
plt.figure(figsize=(7,7))
plt.title("AGE DISTRIBUTION OF MALE VICTIMS OF KIDNAPP")
x=plt.pie([m10,m15,m18,m30,m50,ma50],labels=["m(<10years)]","m(10-15 years)","m(15-18 years)","m(18-30 years)","m(30-50 years)","m(>50years)"],autopct="%1.1f%%",shadow=True,explode=(0.1,0.1,0.1,0.1,0.1,0.1))
plt.show()
sns.set()
plt.figure(figsize=(11,5))
plt.title("STATE WISE DISTRIBUTION OF KIDNAPP CASES IN INDIA")
plt.xlabel("STATES")
plt.ylabel("NO OF CASESE REPORTED")
plt.xticks(rotation=75)
plt.bar(du,re)
plt.show()
plt.figure(figsize=(8,5))
plt.title("years vs no of cases analysis")
plt.xlabel("years")
plt.ylabel("no of cases reported")
plt.plot(years,cases)
plt.show()
fig1,fi=plt.subplots(figsize=(9,9))
fi.pie(w,labels=o,autopct="%1.1f%%",explode=(0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1),pctdistance=0.85)
cir=plt.Circle((0,0),0.7,fc="white")
fig=plt.gcf()
fig.gca().add_artist(cir)
fi.axis("equal")
plt.tight_layout()
plt.show()


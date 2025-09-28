from random import choice

c=float(input())
print(c,"C=",round((c*9/5)+32,2),"F")
print(c,"C=",round(c+273.15,2),"K")

n=int(c)
if n%2==0:
    print("Четное")
else:
    print("Нечетное")
if n>0:
    print("+")
elif n==0:
    print(0)
else:
    print("-")
if 10<=n<=50:
    print("Yes")
else:
    print("No")

b="AQWERTYUIOPSDFGHJKLZXCVBNM"
num="1234567890"
spe="!@#$%^&*"
k=l=p=""
for i in range(3):
    k+=choice(b)
    l+=choice(num)
for i in range(2):
    p += choice(spe)
print(k,l,p)

a=input().lower()
kp=dict()
for i in a:
    if i in kp:
        kp[i]+=1
    else:
        kp[i]=1
print(sorted(kp.items())[:3])

n=int(input())
p=[i for i in range(n+1)]
p[1]=0
i=2
while i<=n:
    if p[i]!=0:
        j=i+i
        while j<=n:
            p[j]=0
            j+=i
    i+=1
p=[i for i in p if i!=0]
print(p)

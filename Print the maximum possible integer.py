n=int(input())
s=str(n)
ss,r,cou=0,0,0
for i in s:
    ss+=int(i)
for i in range(n-1,0,-1):
    for j in str(i):
        r+=int(j)
    if(r>ss):
        cou=1
        print(i)
        break
    r=0
    cou=0
if(cou==0):
    print(n)
    
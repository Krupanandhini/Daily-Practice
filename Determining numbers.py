from collections import Counter
n=int(input())
ar=list(map(int,input().split()))
c=dict(Counter(ar))
l=[]
for key,value in c.items():
    if(value==1):
        l.append(key)
l.sort()
print(l[0],l[1])



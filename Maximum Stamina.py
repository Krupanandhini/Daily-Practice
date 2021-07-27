from collections import deque
n=int(input())
ar=list(map(int,input().split()))
l,lst=[],[]
num=0
d=deque(ar)
for j in range(len(list(d))):
    for i in range(len(list(d))):
        if(d[i]>num):
            l.append(d[i])
            num=d[i]
    lst.append(l)
    d.popleft()
    l=[]
    num=0
sum=0
res=[]
for i in lst:
    for j in i:
        sum=sum^j
    res.append(sum)
    sum=0
res.sort(reverse=True)
print(res[0])

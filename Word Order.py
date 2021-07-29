from collections import Counter
n=int(input())
l,cou,st=[],0,''
for i in range(n):
    l.append(input())
c=Counter(l)
for i in c:
    cou+=1
    st+=str(c[i])+' '
print(cou)
print(st)

n=input()
l,ll=[],[]
cou,gou=0,0
for i in n:
    l.append(i)
l.sort()
for i in range(len(n)):
    if(n[i]==l[i]):
        cou+=1
    else:
        gou+=1
if(cou==0):
    print(len(l))
elif(gou>=(len(l)//2)):
    print(cou)
else:
    print(gou)
    
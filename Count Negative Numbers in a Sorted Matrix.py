n=input()
cou=0
s=""
x=n.split(' ')
for i in x:
    s+=i
res=s.split('#')
for i in res:
    for j in i:
        if(j=='-'):
            cou+=1
print(cou)


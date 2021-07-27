n=list(map(int,input().split()))
ar=list(map(int,input().split()))
cou,gou=0,0
for i in range(n[0]):
    if(gou==2): break
    else:
        if(ar[i]<=n[1]): cou+=1   
        else: gou+=1
print(cou)
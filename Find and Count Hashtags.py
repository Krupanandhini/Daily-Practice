from collections import Counter
n=int(input())
l,lst=[],[]
for i in range(n):
    l.append(input().split())
for i in l:
    for j in i:
        if(j[0]=='#'):
            lst.append(j)
lst.sort()
x=Counter(lst).most_common(5)
for i in x:
    print(i[0])



from collections import defaultdict

n, m = map(int, input().split(' '))

i1,i2= [],[]
d = defaultdict(list)

for i in range(n):
    d[input()].append(i+1)
    
for i in range(m):
    i2.append(input())
    
for i in i2:    
    if i in d:
        print(*d[i])
    else:
        print(-1)


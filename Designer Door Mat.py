n=input().split()
for i in range(1,int(n[0]),2):
    print(('.|.'*i).center(int(n[1]),'-'))
print('WELCOME'.center(int(n[1]),'-'))
for i in range(int(n[0])-2,0,-2):
    print(('.|.'*i).center(int(n[1]),'-'))

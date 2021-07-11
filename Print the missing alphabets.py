n=input().lower()
s='abcdefghijklmnopqrstuvwxyz'
for i in s:
    if(i.isdigit()):
        pass
    elif(i not in n):
        print(i,end='')



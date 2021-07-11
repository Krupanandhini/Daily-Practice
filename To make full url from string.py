n=input()
s=n.split("#")
t=""
for i in range(len(s)):
    if(i==0 or i==1):
        t+=s[i]+'.'
    else:
        t+=s[i]+'/'
print('https://'+t)
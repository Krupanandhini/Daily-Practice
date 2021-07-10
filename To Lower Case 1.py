n = input()
res=""
for i in n:
    if(i.isupper()):
        res+=i.lower()
    else:
        res+=i
print(res)
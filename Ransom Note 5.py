ran=input()
mag=input()
cou=0
s=""
for i in mag:
    if(i==ran):
        print('true')
        cou=1
    else:
        s+=i
        if(s==ran):
            print('true')
            cou=1
if(cou==0):
    print('false')


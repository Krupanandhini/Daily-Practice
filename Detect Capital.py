n=input()
nn=n[1:]
if(n.isupper() or n.islower() or (n[0].isupper and nn.islower())):
    print('true')
else:
    print('false')
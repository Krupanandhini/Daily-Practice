def solve(s):
    st=''
    for i in range(len(s)):
        if(i==0 or s[i-1]==" "):
            st+=s[i].upper()
        else:
            st+=s[i]
    return st
    

def wrap(string, max_width):
    s,res="",""
    l=[]
    for i in range(len(string)):
        s+=string[i]
        if(len(s)%max_width==0):
            l.append(s)
            s="" 
    l.append(s)
    for i in l:
        res+=i+'\n'
    return res

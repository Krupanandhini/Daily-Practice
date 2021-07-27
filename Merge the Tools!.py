def merge_the_tools(string, k):
    lst=[]
    l=len(string)//k
    for i in range(0,len(string),k):
        x=string[i:i+k]
        t=""
        for i in x:
            if(i in t):
                pass
            else:
                t+=i
        print(t)
            

s=input()
find=s.find('#')
num=find+1
length=int(s[num])
l, li=[], []
for i in range(length):
    l.append(i+1)
for i in range(len(s)):
    if s[i] in '1234567890' and i!=len(s)-1:    
        li.append(int(s[i]))
lists, lis=[], []
st=""
for i in l:
    if lis!=li:
        if i in li:
            st+="\"Push\","
            lis.append(i)
        else:
            st+=("\"Push\",")
            st+=("\"Pop\",")
strip=st.rstrip(',')
print("["+strip+"]")


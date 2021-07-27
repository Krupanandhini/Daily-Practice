def swap_case(s):
    res=""
    for i in s:
        if(i.isupper()):
            res+=i.lower()
        else:
            res+=i.upper()
    return res


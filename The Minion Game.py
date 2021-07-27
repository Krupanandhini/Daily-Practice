def minion_game(string):
    s,su=0,0
    lenn=len(string)
    for i in range(len(string)):
        if(string[i] in 'AEIOU'):
            s+=lenn
        else:
            su+=lenn
        lenn-=1
    if(su>s):
        print('Stuart',su)
    elif(s>su): print('Kevin',s)
    else: print('Draw')
   

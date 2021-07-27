def count_substring(string, sub_string):
    cou=0
    for i in range(len(string)):
        if(string[i:i+len(sub_string)]==sub_string):
            cou+=1
    return cou


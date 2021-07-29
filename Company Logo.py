from collections import Counter

if __name__ == '__main__':
    s = sorted(input())
    res=Counter(s).most_common(3)
    for i in res:
        print(*i)

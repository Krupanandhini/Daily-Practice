from collections import deque

d = deque()
N = int(input())

for i in range(N):
    io = input().split()
    if(io[0] == 'append'):
        d.append(io[1])
    elif(io[0] == 'popleft'):
        d.popleft()
    elif(io[0] == 'appendleft'):
        d.appendleft(io[1])
    elif(io[0] == 'pop'):
        d.pop()

print(' '.join(d))

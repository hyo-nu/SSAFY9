from collections import deque
import sys;sys.stdin = open('input.txt')
# F,  S,  G,   U,  D
# 총,현재,도착,위로,아래로
'''
10 1 10 2 1
6
'''
F,S,G,U,D = map(int,input().split())
Q = deque()
Q.append(S)
vi = [0] * (F+1)
vi[S] = 1

while Q:
    now = Q.popleft()
    for d in (U,-D):
        next = now + d
        if 1 <= next <= F and not vi[next]:
            vi[next] = vi[now] + 1
            Q.append(next)
if vi[G] : print(vi[G]-1)
else : print('use the stairs')
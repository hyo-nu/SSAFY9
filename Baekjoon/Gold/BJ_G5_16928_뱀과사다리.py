import sys;sys.stdin=open('input.txt')
from collections import deque

def BFS():
    while Q:
        now = Q.popleft()
        tmp = vi[now]
        while G[now]:
            if G[now][0] > now:
                if vi[G[now][0]] == -1:
                    now = G[now][0]
                    vi[now] = tmp
            else :
                now = G[now][0]
                if vi[now] == -1: vi[now] = tmp

        for dice in range(1,7):
            next = now + dice
            if next <= 100 and vi[next] == -1:
                vi[next] = vi[now] + 1
                Q.append(next)

        if vi[100] != -1:break

N,M = map(int,input().split())
G = [[]for _ in range(101)]
for x,y in [map(int,input().split()) for _ in range(N)]: G[x].append(y)
for u,v in [map(int,input().split()) for _ in range(N)]: G[u].append(v)

Q = deque()
Q.append(1)
vi = [-1] * 101
vi[1] = 0
BFS()
print(vi[100])
for i,v in enumerate(vi):
    print(f'{i} : {v}')


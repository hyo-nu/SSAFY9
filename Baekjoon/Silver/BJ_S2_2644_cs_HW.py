import sys;sys.stdin=open('input.txt')
from collections import deque

def BFS(SP):
    global vi
    Q = deque()
    Q.append(SP)
    vi = [0] * (N + 1)
    vi[SP] = 1

    while Q:
        v = Q.popleft()
        for w in G[v]:
            if not vi[w]:
                Q.append(w)
                vi[w] = vi[v] + 1


N = int(input())
SP, EP = map(int,input().split())
G = [[] for _ in range(N+1)]

for _ in range(int(input())):
    u,v = map(int,input().split())
    G[u].append(v)
    G[v].append(u)

BFS(SP)
print(vi[EP]-1)



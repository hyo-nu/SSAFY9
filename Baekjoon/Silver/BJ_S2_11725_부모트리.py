import sys;sys.stdin = open('input.txt')
from collections import deque
input = sys.stdin.readline
def BFS(v):
    Q.append(v)
    vi[v] = 1
    while Q:
        v = Q.popleft()
        for w in G[v]:
            if not vi[w]:
                vi[w] = 1
                p[w] = v
                Q.append(w)

N = int(input())
G = [[] for _ in range(N + 1)]

for _ in range(N-1):
    u, v = map(int,input().split())
    G[u].append(v)
    G[v].append(u)

vi = [0] * (N + 1)
p = [0] * (N + 1)
Q = deque()
for i in range(1,N+1):
    if not vi[i]:
        BFS(i)
for i in range(2,N+1):
    print(p[i])
import sys;sys.stdin=open('input.txt')
from collections import deque
input = sys.stdin.readline

V = int(input())
E = int(input())

# G = [set() for _ in range(V + 1)]
G = {i:set() for i in range(V + 1)}

for _ in range(E):
    u,v,weight = map(int,input().split())
    G[u].add((v,weight))

S, E = map(int,input().split())
Q = deque()
Q.append(S)
D = [0xffffffffffff] * (V + 1)
D[S] = 0

while Q:
    u = Q.popleft()
    for v, weight in G[u]:
        if D[v] > D[u] + weight:
            D[v] = D[u] + weight
            Q.append(v)
print(D[E])

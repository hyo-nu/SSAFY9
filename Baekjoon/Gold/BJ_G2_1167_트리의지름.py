import sys;sys.stdin=open('input.txt')
from collections import deque
input = sys.stdin.readline
V = int(input())
G = [[] for _ in range(V + 1)]

for _ in range(1,V+1):
    U, *E, mi = map(int,input().split())
    for i in range(0,len(E),2):
        G[U].append((E[i],E[i+1]))
Q = deque()
Q.append(1)
D = [0] * (V + 1)

while Q:
    u = Q.popleft()
    for v, weight in G[u]:
        if D[v] < D[u] + weight:
            D[v] = D[u] + weight
            Q.append(v)

print(max(D))
import sys;sys.stdin=open('input.txt')
from collections import deque

N, distance = map(int,input().split())
G=[]

for _ in range(N):
    u,v,weight = map(int,input().split())
    G.append((u,v,weight))

Q = deque()
Q.append(0)
D = [i for i in range(distance+2)]
D[0] = 0

for u, v,weight in G:
    if D[v] > D[u] + weight:
        D[v] = D[u] + weight
        Q.append(v)
print(D)
for i in range(distance,-1,-1):
    if D[i] != i:
        result = distance - i + D[i]
        break
print(result)
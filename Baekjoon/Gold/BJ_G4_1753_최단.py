import sys
from heapq import heappop, heappush
input = sys.stdin.readline

V, E = map(int,input().split())
K = int(input())
# G = [set() for _ in range(V + 1)]
G = [{} for i in range(V + 1)]

for _ in range(E):
    u,v,weight = map(int,input().split())
    if v not in G[u] : G[u][v] = weight
    else : G[u][v] = min(G[u][v],weight)
h = []
heappush(h,(0,K))
D = [0xffffffff] * (V + 1)
D[K] = 0
while h:
    d, u = heappop(h)
    if D[u] < d :
        continue
    for v, weight in G[u].items():
        if D[v] > d + weight:
            D[v] = d + weight
            heappush(h,(d + weight , v))

for i in range(1,V+1):
    if D[i] == 0xffffffff : print('INF')
    else : print(D[i])

import sys;sys.stdin=open('input.txt')
from heapq import heappop, heappush

V,E = map(int,input().split())
G = [[] for _ in range(V + 1)]

for _ in range(E):
    u,v,weight = map(int,input().split())
    G[u].append((v,weight))
    G[v].append((u,weight))

SP, EP = map(int,input().split())
h = []
heappush(h,(0,1))
D = [0xffffffff] * (V + 1)
D[1] = 0
stop = 0

while h:
    d, u = heappop(h)
    if D[u] < d: continue
    for v, weight in G[u]:
        if D[v] > d + weight:
            D[v] = d + weight
            heappush(h,(d + weight,v))
    #     if D[EP] != 0xffffffff and D[SP] != 0xffffffff:
    #         stop = 1 ; break
    # if stop : break
# if stop : print(D[EP]+D[SP]-1)
# else : print(-1)
print(D)

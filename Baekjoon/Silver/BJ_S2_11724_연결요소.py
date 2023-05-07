import sys;sys.stdin=open('input.txt')

input = sys.stdin.readline

def DFS(v):
    S.append(v)
    while S:
        for w in G[v]:
            if not vi[w]:
                S.append(v)
                vi[w] = 1
                v = w
                break
        else:
            v = S.pop()
    return 1

V, E = map(int,input().split())
G = [[] for _ in range(V+1)]

for _ in range(E):
    u, v = map(int,input().split())
    G[u].append(v)
    G[v].append(u)

vi = [0] * (V+1)
S = []
cnt = 0
for v in range(1,V+1):
    if not vi[v]:
        vi[v] = 1
        cnt += DFS(v)

print(cnt)
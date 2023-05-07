import sys ; sys.stdin = open('input.txt')

def DFS(V):
    S = []
    S.append(V)
    visited = [0] * (N + 1)
    visited[V] = 1
    result = [V]
    while S:
        for w in G[V]:
            if visited[w] == 0:
                visited[w] = 1
                S.append(V)
                V = w
                result.append(V)
                break
        else:
            V = S.pop()
    return result
def BFS(V):
    Q = []
    Q.append(V)
    visited = [0] * (N + 1)
    visited[V] = 1
    result = [V]

    while Q:
        V = Q.pop(0)
        for w in G[V]:
            if visited[w] == 0:
                visited[w] = 1
                Q.append(w)
                result.append(w)
    return result

N, M, start = map(int,input().split())

G = [[]for _ in range(N+1)]
for i in range(M):
    u,v = map(int,input().split())
    G[u].append(v)
    G[v].append(u)

for i in G:
    i.sort()

print(*DFS(start))
print(*BFS(start))
Test = int(input())

for TC in range(Test):
    Ver, Edge = map(int, input().split())
    G = [[] for _ in range(Ver + 1)]

    for _ in range(Edge):
        u, v = map(int, input().split())
        G[u].append(v)
        G[v].append(u)

    start, end = map(int, input().split())

    Q = []
    visited = [0] * (Ver + 1)
    Q.append(start)
    visited[start] = 1

    while Q:
        V = Q.pop(0)
        for w in G[V]:
            if not visited[w]:
                Q.append(w)
                # visited[w] = 1
                # V = w
                visited[w] = visited[V] + 1

    if visited[end]:
        visited[end] -= 1
    print(f'#{TC+1}',visited[end])
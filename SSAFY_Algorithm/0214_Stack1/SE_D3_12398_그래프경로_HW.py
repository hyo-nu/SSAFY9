Test = int(input())

for T in range(Test):
    V, E = map(int,input().split()) # 정점(Vertex), 간선(Edge)

    G = [[] for _ in range(V+1)]

    for e in range(E):
        u,v = map(int,input().split())
        G[u].append(v)

    start,end = map(int,input().split())

    S = []
    visited = [0] * (V+1)
    S.append(start)
    visited[start] = 1
    land = 0

    while S:
        for i in G[start]:
            if not visited[i]:
                S.append(start)
                visited[i] = 1
                start = i
                if start == end : land += 1
                break
        else:
            start = S.pop()
    print(f'#{T + 1}',end = ' ')
    if land > 0 : print(1)
    else : print(0)
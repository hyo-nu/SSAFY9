def find_set(x):
    if x != p[x]:
        p[x] = find_set(p[x])
    return p[x]

Test = int(input())

for TC in range(Test):
    N, M = map(int,input().split())
    arr = list(map(int,input().split()))
    p = [i for i in range(N + 1)]
    G = []

    ans = N
    for i in range(0,M*2,2):
        u, v = arr[i], arr[i+1]
        G.append([u,v])
        a = find_set(u)
        b = find_set(v)
        if a == b:
            continue
        p[a] = b
        ans -= 1
    print(f'#{TC+1}', ans)

#==============================================
def DFS(v):
    visited[v] = 1
    for w in G[v]:
        if not visited[w]:
            DFS(w)

Test = int(input())

for TC in range(Test):
    N, M = map(int,input().split())
    arr = list(map(int,input().split()))
    p = [i for i in range(N + 1)]
    G = [[] for i in range(N + 1)]

    for i in range(0, M * 2, 2):
        u, v = arr[i], arr[i + 1]
        G[u].append([v])
        G[v].append([u])

    visited = [0] * (N + 1)

    ans = 0
    for i in range(1 , N + 1):
        if not visited[i]:
            ans += 1
            DFS(i)
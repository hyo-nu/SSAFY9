def BFS(SP):
    Q = []
    Vi = [0] * 101
    Q.append(SP)
    Vi[SP] = 1
    ans = SP
    while Q:
        NP = Q.pop(0)
        if Vi[ans] < Vi[NP] or Vi[ans] == Vi[NP] and ans < NP:
            ans = NP
        for w in G[NP]:
            if Vi[w] == 0:
                Q.append(w)
                Vi[w] = Vi[NP] + 1
    return ans

Test = 10

for T in range(Test):
    E, SP = map(int,input().split())
    Edge = list(map(int,input().split()))
    G = [[] for _ in range(101)]

    for i in range(0,E,2):
        u,v = Edge[i] , Edge[i+1]
        G[u].append(v)

    print(f'#{T+1}',BFS(SP))
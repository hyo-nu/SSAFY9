def DFS(n,lst):
    if n == M:
        ans.append(lst)
        return
    for i in range(1,N+1):
        if v[i] == 0:
            v[i] = 1
            DFS(n+1,lst+[i])
            v[i] = 0

N,M = map(int,input().split())

v = [0] * (N+1)
ans = []

DFS(0,[])
for lst in ans:
    print(*lst)
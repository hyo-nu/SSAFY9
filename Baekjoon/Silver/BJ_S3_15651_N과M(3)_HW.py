def DFS(n, lst):
    if n == M:
        return ans.append(lst)

    for i in range(1, N + 1):
        if v[i] == 0:
            DFS(n + 1, lst + [i])

N, M = map(int, input().split())
v = [0] * (N + 1)
ans = []
DFS(0, [])

for lst in ans:
    print(*lst)

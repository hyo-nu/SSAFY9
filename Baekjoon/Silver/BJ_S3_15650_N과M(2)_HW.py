def dfs(n,lst):
    if n > N:
        # if len(lst) == M:
        ans.append(lst)
        return

    dfs(n+1,lst+[n])
    dfs(n+1,lst)


N, M = map(int, input().split())
ans = []
dfs(1, [])

for lst in ans:
    print(*lst)

#====================================

# def DFS(n, lst):
#     if n == M:
#         for i in range(M - 1):
#             if lst[i] > lst[i + 1]:
#                 break
#         else:
#             return ans.append(lst)
#
#     for i in range(1, N + 1):
#         if v[i] == 0:
#             v[i] = 1
#             DFS(n + 1, lst + [i])
#             v[i] = 0
#
#
# N, M = map(int, input().split())
# v = [0] * (N + 1)
# ans = []
# DFS(0, [])
#
# for lst in ans:
#     print(*lst)









import sys;sys.stdin=open('input.txt')
from collections import deque

Test = int(input())

for TC in range(Test):
    N, E = map(int,input().split())
    G = [[] for _ in range(N+1)]

    for _ in range(E):
        u,v,weight = map(int,input().split())
        G[u].append((v,weight))

    Q = deque()
    Q.append(0)
    D = [0xffffff]*(N + 1)
    D[0] = 0

    while Q:
        u = Q.popleft()
        for v,weight in G[u]:
            if D[v] > D[u] + weight:
                D[v] = D[u] + weight
                Q.append(v)

    print(f'#{TC+1}',D[N])



#==================================================
# 교수님 풀이 BFS 버전
# Test = int(input())
#
# for TC in range(Test):
#     N, E = map(int,input().split())
#     G = [[] for _ in range(N+1)]
#
#     for _ in range(E):
#         u, v, weight = map(int,input().split())
#         G[u].append((v,weight))
#
#     Q = deque()
#     Q.append(0)
#     D = [0xfffff] * (N + 1)
#     D[0] = 0
#
#     while Q:
#         u = Q.popleft()
#         for v, weight in G[u]:
#             if D[v] > D[u] + weight:
#                D[v] = D[u] + weight
#                Q.append(v)
#
#     print(f'#{TC+1}', D[N])
#
#
# # 교수님 풀이 DFS 버전
# def DFS(u):
#     if D[u] >= D[N]:
#         return
#     for v, weight in G(u):
#         if D[v] > D[u] + weight:
#             D[v] = D[u] + weight
#             DFS(v)
# DFS(0)


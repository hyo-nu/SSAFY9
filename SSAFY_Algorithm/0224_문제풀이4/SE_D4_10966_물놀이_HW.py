import time
start = time.time()

import sys ; sys.stdin = open('input2.txt')

from collections import deque
def BFS(Q):
    dr = [0, 1, 0, -1]#우하좌상
    dc = [1, 0, -1, 0]
    Sum = 0
    while Q:
        NP = Q.popleft()
        for d in range(4):
            nr,nc = NP[0] + dr[d] , NP[1] + dc[d]
            if 0 <= nr < N and 0 <= nc < M and pool[nr][nc] == -1:
                pool[nr][nc] = pool[NP[0]][NP[1]] + 1
                Q.append([nr,nc])
                Sum += pool[nr][nc]
    return Sum

Test = int(input())
for T in range(Test):
    N,M = map(int,input().split())
    pool = [[-1] * M for _ in range(N)]
    Q = deque()
    # 문자에서 숫자로 변환
    for r in range(N):
        WL = input()
        for c in range(M):
            if WL[c] == 'W':
                pool[r][c] = 0
                Q.append([r, c])

    print(f'#{T + 1}',BFS(Q))

print(time.time() - start)













#
# #================
# import sys;sys.stdin = open('input.txt')
# from collections import deque
# import time
#
# start = time.time()
#
# def BFS():
#     global Sum
#     dr = [0, 1, 0, -1]  # 우하좌상
#     dc = [1, 0, -1, 0]
#     Sum = 0
#     while Q:
#         NP = Q.popleft()
#         for d in range(4):
#             nr = NP[0] + dr[d]
#             nc = NP[1] + dc[d]
#             if 0 <= nr < N and 0 <= nc < M and pool[nr][nc] == 'L':
#                 pool[nr][nc] = pool[NP[0]][NP[1]] + 1
#                 Q.append([nr,nc])
#                 Sum += pool[nr][nc]
#
# Test = int(input())
#
# for T in range(Test):
#     N, M = map(int, input().split())
#     pool = [list(input()) for _ in range(N)]
#     Q = deque()
#     # 1 <= N(row),M(col) <= 1000
#     for r in range(N):
#         for c in range(M):
#             if pool[r][c] == 'W':
#                 pool[r][c] = 0
#                 Q.append([r, c])
#     BFS()
#     print(f'#{T + 1}',Sum)
#
# print(time.time() - start)
#
# #======================================
# # def BFS(Wcnt):
# #     dr = [0, 1, 0, -1]  # 우하좌상
# #     dc = [1, 0, -1, 0]
# #     Lcnt = 0
# #     while Q:
# #         NP = Q.pop(0)
# #
# #         for d in range(4):
# #             nr = NP[0] + dr[d]
# #             nc = NP[1] + dc[d]
# #             if 0 <= nr < N and 0 <= nc < M and pool[nr][nc] == 'L':
# #                 if not vi[nr][nc]:
# #                     vi[nr][nc] = vi[NP[0]][NP[1]] + 1
# #                     Q.append([nr,nc])
# #                     Lcnt += 1
# #         if Lcnt + Wcnt == M * N: return
# #
# # Test = int(input())
# #
# # for T in range(Test):
# #     N, M = map(int, input().split())
# #     pool = [list(input()) for _ in range(N)]
# #     vi = [[0] * M for _ in range(N)]
# #     Q = []
# #     Wcnt = 0
# #     # 1 <= N(row),M(col) <= 1000
# #     for r in range(N):
# #         for c in range(M):
# #             if pool[r][c] == 'W':
# #                 vi[r][c] = 1
# #                 Wcnt += 1
# #                 Q.append([r, c])
# #     BFS(Wcnt)
# #     Sum = sum([sum(lst) for lst in vi])
# #     print(f'#{T+1}',Sum-M*N)
# #
# # print(time.time() - start)
#
# from collections import deque
#
# def BFS():
#     dr = [0, 1, 0, -1]  # 우하좌상
#     dc = [1, 0, -1, 0]
#
#     while Q:
#         NP = Q.popleft()
#         for d in range(4):
#             nr = NP[0] + dr[d]
#             nc = NP[1] + dc[d]
#             if 0 <= nr < N and 0 <= nc < M and pool[nr][nc] == 0:
#                 if not vi[nr][nc]:
#                     vi[nr][nc] = vi[NP[0]][NP[1]] + 1
#                     Q.append([nr, nc])
#
# Test = int(input())
#
# for T in range(Test):
#     # N : 행 , M ; 열
#     N, M = map(int, input().split())
#     pool = [list(input()) for _ in range(N)]
#     vi = [[0] * M for _ in range(N)]
#     Q = deque()
#
#     for i in range(N):
#         for j in range(M):
#             if pool[i][j] == 'W':
#                 pool[i][j] = 1
#             elif pool[i][j] == 'L':
#                 pool[i][j] = 0
#
#     for r in range(N):
#         for c in range(M):
#             if pool[r][c] == 1:
#                 vi[r][c] = 0
#                 Q.append([r, c])
#     BFS()
#
#     Sum = sum([sum(lst) for lst in vi])
#     print(f'#{T + 1}', Sum)
#
#

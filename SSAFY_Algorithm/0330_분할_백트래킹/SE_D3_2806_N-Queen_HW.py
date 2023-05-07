# def nQueen(r):
#     if r == N:
#         return
#     else:
#         for c in range(r,N):
#             point = (r,c)
#             nQueen(r+1)
#
# Test = int(input())
#
# for TC in range(Test):
#     N = int(input())
#     nQueen(0)
#
# #===================================
# # 교수님
# def promising(r,c):
#     for i in range(r):
#         if abs(i-r) == abs(cols[i]-c):
#             return False
#     return True
#
# def nQueen(k):
#     if k == N:
#         global ans ; ans += 1
#         return
#     else:
#         for i in range(N):
#             if used[i] : continue
#             if not promising(k,i): continue
#             used[i] = 1
#             cols[k] = i   # k번행, i열에 퀸을 위치
#             nQueen(k + 1)
#             used[i] = 0
#
# Test = int(input())
#
# for TC in range(Test):
#     N = int(input())
#     used = [0] * N
#     cols = [0] * N
#     ans = 0
#     nQueen(0)
# #===================================
# # 교수님
# def promising(r,c):
#     for i in range(r):
#         if abs(i-r) == abs(cols[i]-c):
#             return False
#     return True

def nQueen(k):
    if k == N:
        global ans ; ans += 1
    else:
        for i in range(N):
            a, b = k + i , (k - i) + N
            if used[i] or line1[a] or line2[b]: continue
            used[i] = line1[a] = line2[b] = 1
            nQueen(k + 1)
            used[i] = line1[a] = line2[b] = 0

N = int(input())
used = [0] * N
line1 = [0] * (N << 1)
line2 = [0] * (N << 1)
ans = 0
nQueen(0)
print(ans)








#===========================================

# def promising(i,j):
#     for di, dj in [[-1,-1],[-1, 0],[-1,1]]:
#         ni, nj = i + di, j + dj
#         while 0 <= ni < N and 0 <= nj < N:
#             if board[ni][nj]:
#                 return 0
#             ni, nj = ni+di , nj+dj
#     return 1
#
#
# def f(i,N):
#     global cnt
#     if i == N:
#         cnt += 1
#     else:
#         for j in range(N):
#             if promising(i,j):
#                 board[i][j] = 1
#                 f(i+1,N)
#                 board[i][j] = 0
#
# T = int(input())
#
# for TC in range(1, T+1):
#     N = int(input())
#
#     board = [[0]*N for _ in range(N)]
#     cnt = 0
#     f(0,N)
#     print(f'#{TC}',cnt)




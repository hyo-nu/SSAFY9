import sys;sys.stdin = open('input.txt')
# 흰
# 파
# 빨
Test = int(input())

for T in range(Test):
    # 3 <= N,M <= 50
    N, M = map(int, input().split())
    flag = [list(input()) for _ in range(N)]

    # 3분할
    Min = N * M
    for i in range(1, N):
        for j in range(i + 1, N):
            # White
            cnt = 0
            for r in range(0, i):
                for c in range(M):
                    if flag[r][c] != 'W' : cnt += 1
            # Blue
            for r in range(i, j):
                for c in range(M):
                    if flag[r][c] != 'B': cnt += 1
            # Red
            for r in range(j, N):
                for c in range(M):
                    if flag[r][c] != 'R': cnt += 1

            if Min > cnt:
                Min = cnt

    print(f'#{T+1}',Min)

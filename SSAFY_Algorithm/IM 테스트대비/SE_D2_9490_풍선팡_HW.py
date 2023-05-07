import sys;sys.stdin = open('input.txt')
Test = int(input())

for TC in range(Test):
    N, M = map(int,input().split())
    G = [list(map(int,input().split())) for _ in range(N)]

    dr = [0, 1, 0,-1]
    dc = [1, 0,-1, 0]
    Max = 0
    for r in range(N):
        for c in range(M):
            Sum = G[r][c]
            for i in range(1,G[r][c]+1):
                for d in range(4):
                    nr = r + dr[d] * i
                    nc = c + dc[d] * i
                    if 0 <= nr < N and 0 <= nc < M:
                        Sum += G[nr][nc]
            if Max < Sum : Max = Sum
    print(f'#{TC+1}',Max)
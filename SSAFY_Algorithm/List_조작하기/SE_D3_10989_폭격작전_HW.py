# 폭격작전
import sys ; sys.stdin = open('input.txt')

def Kill(R, C, bomb):
    kill[R][C] = Map[R][C]
    dr = [0, 1, 0, -1]  # 우하좌상
    dc = [1, 0, -1, 0]
    for d in range(4):
        for b in range(1,bomb+1):
            nr = R + dr[d] * b
            nc = C + dc[d] * b
            if 0 <= nr < N and 0 <= nc < N:
                kill[nr][nc] = Map[nr][nc]

Test = int(input())

for T in range(Test):
    N, M = map(int, input().split())
    Map = [list(map(int, input().split())) for _ in range(N)]
    kill = [[0] * N for _ in range(N)]

    for _ in range(M):
        R, C, bomb = map(int, input().split())
        Kill(R,C,bomb)

    Sum = 0
    for lst in kill:
        Sum += sum(lst)
    print(f'#{T+1}',Sum)

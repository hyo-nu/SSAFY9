# 오목
import sys;sys.stdin = open('input.txt')

def Win():
    dr = [0, 1, 1, 1, 0]  # 우대하대좌
    dc = [1, 1, 0,-1,-1]

    for r in range(N):
        for c in range(N):
            if con[r][c]=='o':
                for d in range(5):
                    for i in range(1,5):
                        nr = r + dr[d] * i
                        nc = c + dc[d] * i
                        if 0 <= nr <N and 0 <= nc < N:
                            if con[nr][nc] == 'o':pass
                            else:break
                        else : break
                    else : return 'YES'
    return 'NO'

Test = int(input())

for T in range(Test):
    N = int(input())
    con = [list(input()) for _ in range(N)]

    print(f'#{T+1}',Win())



Test = int(input())

for T in range(Test):
    N,M = map(int,input().split())
    pari = [list(map(int,input().split())) for _ in range(N)]

    pari_max = 0
    for i in range(N-M+1):
        for j in range(N-M+1):
            pari_cnt = 0
            for r in range(M):
                for c in range(M):
                    pari_cnt += pari[i+r][j+c]
            if pari_max < pari_cnt: pari_max = pari_cnt
    print(f'#{T+1}',pari_max)
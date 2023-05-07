Test = int(input())

for T in range(Test):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

    Max_r = 0
    for r in range(N):
        length_r = 0
        for c in range(M):
            if arr[r][c] == 1 : length_r += 1
            else : length_r = 0
            if Max_r <= length_r : Max_r = length_r

    Max_c = 0
    for r in range(M):
        length_c = 0
        for c in range(N):
            if arr[c][r] == 1 : length_c += 1
            else : length_c = 0
            if Max_c <= length_c : Max_c = length_c

    print(f'#{T+1}',max(Max_r,Max_c))
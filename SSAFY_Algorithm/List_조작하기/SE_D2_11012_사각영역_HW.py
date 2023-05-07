import sys ; sys.stdin = open('input.txt')

Test = int(input())

for T in range(Test):
    N, M = map(int,input().split())
    arr = [list(map(int,input().split()))for _ in range(N)]
    paper = [[0]*N for _ in range(N)]

    for _ in range(M):
        r,c,Len = map(int,input().split())
        Len_r = Len_c = Len
        if r + Len > N : Len_r = N - r
        if c + Len > N : Len_c = N - c

        for i in range(Len_r):
            for j in range(Len_c):
                paper[r+i][c+j] = arr[r+i][c+j]

    result = 0
    for lst in paper:
        result += sum(lst)

    print(f'#{T+1}',result)


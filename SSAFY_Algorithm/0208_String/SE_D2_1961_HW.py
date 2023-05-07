Test = int(input())
for T in range(Test):
    N = int(input())
    arr = [list(map(int,input().split())) for _ in range(N)]

    arr1 = [] # [arr[N-c-1][r]]
    arr2 = [] # [arr[N-r-1][N-c-1]]
    arr3 = [] # [arr[c][N-r-1]]

    arr1 = [[arr[N-c-1][r] for c in range(N)] for r in range(N)]
    arr2 = [[arr[N-r-1][N-c-1] for c in range(N)] for r in range(N)]
    arr3 = [[arr[c][N - r - 1] for c in range(N)] for r in range(N)]

    print(f'#{T + 1}')
    for r in range(N):
        print(*arr1[r],sep ='', end = ' ')
        print(*arr2[r],sep ='', end = ' ')
        print(*arr3[r],sep ='', end = ' ')
        print()
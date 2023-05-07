# 둘
Test = 10

for T in range(Test):
    TC = int(input())
    N = 100
    arr = [list(map(int,input().split())) for _ in range(N)]
    cross_sum = 0
    Max = 0

    for i in range(N):
        row_sum = 0
        column_sum = 0
        for j in range(N):
            row_sum += arr[i][j] # 열 합값 계산
            column_sum += arr[j][i] # 행 합값 계산
            if i==j : cross_sum += arr[i][j] # 대각선 값 더해가기
        if Max < max(row_sum,column_sum): # 열 행중 큰 값을 Max와 비교
            Max = max(row_sum, column_sum)
    if Max < cross_sum:
        Max = cross_sum
    print(f'#{T+1}',Max)



#처음
Test = 10

for T in range(Test):
    T_num = int(input())
    lst_2 = []
    max_lst = []
    for _ in range(100):
        values = list(map(int,input().split()))
        lst_2.append(values)
        max_lst.append(sum(values)) # 행 합값 추가
    # 열 합값 + 대각선 합값 추가
    diag_sum = 0
    for r in range(100):
        row_sum = 0
        for c in range(100):
            row_sum += lst_2[c][r]
            if r == c:
                diag_sum += lst_2[r][c]
        max_lst.append(row_sum)
    max_lst.append(diag_sum)
    max_lst.sort()
    print(f'#{T_num} {max_lst[-1]}')
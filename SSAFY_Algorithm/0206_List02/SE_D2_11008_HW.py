# 둘
Test = int(input())

for T in range(Test):
    N = int(input())

    arr = [list(map(int,input().split()))for _ in range(N)]

    dr = [-1, 0, 1, 0] #상좌하우
    dc = [ 0,-1, 0, 1]

    Max = 0
    for r in range(N):
        for c in range(N):
            Sum = 0

            for d in range(4):
                if 0 <= r+dr[d] < N and 0 <= c+dc[d] < N:
                    Sum += arr[r+dr[d]][c+dc[d]]

            if Max < Sum :
                Max = Sum
                nr,nc = r,c
    print(f'#{T+1}',nr, nc, Max)

# 처음
Test = int(input())

for T in range(Test):
    N = int(input())
    nums_lst2 = []
    for n in range(N):
        nums = list(map(int,input().split()))
        nums_lst2.append(nums)

    sum_max = 0
    # 2차원 배열 요소 하나하나 확인
    for c in range(N):
        for r in range(N):
            sum = 0
            for dc,dr in [[-1,0],[0,1],[1,0],[0,-1]]: #상우하좌
                nc,nr = c+dc,r+dr
                if 0 <= nc < N and 0 <= nr < N:
                    sum += nums_lst2[nc][nr]
            if sum_max < sum:
                sum_max = sum
                now_c = c
                now_r = r

    print(f'#{T+1} {now_c} {now_r} {sum_max}')
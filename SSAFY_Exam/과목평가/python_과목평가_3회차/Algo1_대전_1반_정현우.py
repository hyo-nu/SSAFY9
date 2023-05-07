dr = [-1, -1, -1, 0, 1, 1, 1, 0]  # 대상대우대하대좌
dc = [-1, 0, 1, 1, 1, 0, -1, -1]
Test = int(input())

for TC in range(Test):
    N = int(input())
    hi = [list(map(int, input().split())) for _ in range(N)]

    Max = 0     # 봉우리 최대 높이
    Min = 10    # 봉우리 최저 높이
    mt_check = 0
    for r in range(1,N-1):                         # 가장 자리를 제외한 탐색이기에 range(1, N-1)
        for c in range(1,N-1):
           for d in range(8):                      # 중심을 기준으로 8 개의 구역을 탐색
              if hi[r][c] <= hi[r+dr[d]][c+dc[d]]: # 주변에 중심과 같거나 높은 지역이 있다면 break
                  break
           else:                                   # break 없이 다 돌았다. 즉 주변지역이 중심보다 전부 낮다
               high = hi[r][c]                     # 그때의 봉우리 높이
               mt_check += 1                       # 봉우리의 갯수를 카운트
               if Max < high : Max = high          # 봉우리 최대 높이 업데이트
               if Min > high : Min = high          # 봉우리 최저 높이 업데이트

    print(f'#{TC+1}',end = ' ')
    if mt_check > 1 : print(Max-Min)               # 봉우리 갯수가 2개 이상일 경우 높이차 계산
    else: print(-1)                                # 봉우리 갯수가 1, 0개 이면 -1출력
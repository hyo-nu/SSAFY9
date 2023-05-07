def land_point(r, c):
    dr = [-1, -1, -1, 0, 1, 1, 1, 0]  # 대,상,대,우,대,하,대,좌,
    dc = [-1, 0, 1, 1, 1, 0, -1, -1]
    Error = 0
    land_cnt = 0
    for d in range(8):
        if 0 <= r + dr[d] < N and 0 <= c + dc[d] < M: # 검사 위치가 배열 범위 안
            if A[r + dr[d]][c + dc[d]] < A[r][c]: # 주변 지역이 낮으면
                land_cnt += 1 # 카운트
                if land_cnt >= 4: return 1 # 카운트 4이상이면 후본지 선정
    else:
        Error += 1 # 탐색못하는 지역수
        if Error > 4: return 0  # 탐색불가지역

Test = int(input())

for TC in range(Test):
    N, M = map(int, input().split())
    A = [list(map(int, input().split())) for _ in range(N)]

    land_area = 0
    for r in range(N):
        for c in range(M):
            if land_point(r,c) == 1:land_area += 1
    print(f'#{TC+1}',land_area)
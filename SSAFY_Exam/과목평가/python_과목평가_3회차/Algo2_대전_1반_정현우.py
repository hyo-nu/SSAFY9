dr = [0, 1, 0, -1]  # 우 하 좌 상
dc = [1, 0, -1, 0]

Test = int(input())

for TC in range(Test):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    r, c = 0, 0 # 출발지, 왼쪽 윗 칸
    energy = [] # 방향 전환 지점 list

    while True:
        for d in range(4):                                 # 방향을 확인
            if arr[r][c] == d:                             # 해당 지점의 방향이 d인 경우
                if arr[r][c] != arr[r + dr[d]][c + dc[d]]: # 방향 전환이 이루어 졌는지 확인
                    energy.append(arr[r][c])               # 이루어졌으면 에너지 소비이므로 이동 전 방향 저장
                arr[r][c] = '.'                            # 지나온 지점은 '.' 초기화
                r = r + dr[d]                              # 현위치 초기화
                c = c + dc[d]
                break                                      # 이동했으니 나머지 방향 탐색 필요없음
        if arr[r][c] == '.':break                          # 이동한 방향이 '.' 이면 이동 종료

    print(f'#{TC+1}',end=' ')
    print(*energy)                                         # 에너지 소비를 출력한다.

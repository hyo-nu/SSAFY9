# 최단 경로로 도달하는 사다리 위치 탐색
def ladder_min_route(ladder, N):
    distance_min = N * N

    for start in range(N):  # start : 시작위치
        distance = 0  # 이동거리
        r = 0  # 사다리 시작 행
        c = start  # 사다리 시작 열
        if ladder[r][c] == 1:  # 시작지점이 1이여야 시작
            dir = 'STRIGHT'
            while r < N:  # ladder1처럼 이동 and 거리 += 1
                # RIGHT, LEFT
                # 좌로 이동
                if c > 0 and ladder[r][c - 1] == 1 and dir != 'RIGHT':
                    c -= 1  # 좌로 한칸
                    distance += 1
                    dir = 'LEFT'

                # 우로 이동
                elif c < N - 1 and ladder[r][c + 1] == 1 and dir != 'LEFT':
                    c += 1
                    distance += 1
                    dir = 'RIGHT'
                # 전진
                else:
                    r += 1
                    distance += 1
                    dir = 'STRIGHT'

            if distance_min > distance:  # 거리의 최솟값 업데이트
                distance_min = distance
                spot = start  # 거리 최솟값 업데이트시 마다 위치 저장

    return spot  # 최소 루트의 위치 반환


Test = 10

for T in range(Test):
    TC = int(input())
    N = 100
    ladder = [list(map(int, input().split())) for _ in range(N)]

    print(f'#{T + 1}', ladder_min_route(ladder, N))

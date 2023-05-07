# 두번
Test = 10

for T in range(Test):
    TC = int(input())
    N = 100
    ladder = [list(map(int, input().split())) for _ in range(N)]

    for c in range(N):
        if ladder[N - 1][c] == 2:
            spot = c
            break

    r = N - 1
    while r > 0:
        ladder[r][spot] = 0
        # 좌로 이동
        if spot > 0 and ladder[r][spot - 1] == 1:
            spot -= 1  # 좌로 한칸

        # 우로 이동
        elif spot < N - 1 and ladder[r][spot + 1] == 1:
            spot += 1

        # 전진
        else:
            r -= 1

    print(f'#{T + 1}', spot)

# 처음
'''
    0 1 2 3 4 5 6 7 8 9
1 0 0 0 1 0 1 0 0 1
1 0 0 0 1 0 1 1 1 1
1 0 0 0 1 0 1 0 0 1
1 0 0 0 1 1 1 0 0 1
1 0 0 0 1 0 1 0 0 1
1 1 1 1 1 0 1 1 1 1
1 0 0 0 1 0 1 0 0 1
1 1 1 1 1 0 1 0 0 1
1 0 0 0 1 1 1 0 0 1
1 0 0 0 1 0 1 0 0 1
1 0 1 0 0 1 0 1 0 2

'''
Test = 10

for T in range(Test):
    t = int(input())
    N = 100

    ledder_arr = []
    for i in range(N):  # 행 갯수
        ledder = list(map(int, input().split()))
        ledder_arr.append(ledder)

    c = N - 1  # 행 index
    for i in range(c + 1):
        if ledder_arr[c][i] == 2:  # ledder_arr[10][9]
            r = i  # 2일때 열index
    # c = 10 행
    # r = 9 열
    while c >= 0:
        # 오른쪽으로
        ledder_arr[c][r] = 0

        if r < N - 1 and ledder_arr[c][r + 1] == 1:
            r += 1

            # 왼쪽으로
        elif r > 0 and ledder_arr[c][r - 1] == 1:
            r -= 1

        # 위로가자
        else:
            c -= 1
    print(f'#{T + 1}', r)
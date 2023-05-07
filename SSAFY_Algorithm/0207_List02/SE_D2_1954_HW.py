# 두번
Test = int(input())
# Test = 10
dr = [0, 1, 0, -1]  # 우하좌상
dc = [1, 0, -1, 0]

for T in range(Test):
    N = int(input())
    arr = [[0]*N for _ in range(N)]

    row = col = 0
    cnt = 1
    d_idx = 0

    while cnt <= N**2:
        arr[row][col] = cnt
        nr = row + dr[d_idx]
        nc = col + dc[d_idx]
        if nr < 0 or nr >= N or nc < 0 or nc >= N or arr[nr][nc] !=0:
            d_idx = (d_idx+1) % 4
        row += dr[d_idx]
        col += dc[d_idx]
        cnt += 1

    print(f'#{T + 1}')
    for lst in arr:
        print(*lst)

#처음
Test = int(input())

#우하좌상
for T in range(Test):
    N = int(input())
    b_lst = [[0]*(N+2) for _ in range(N+2)]

    for i in range(N+2):
        for j in range(N+2):
            if i ==0 or i == N+1 or j == 0 or j == N+1:
                b_lst[i][j] = 1
    c = 1
    r = 1
    n = 1

    while n <= N*N:
        if b_lst[c][r+1] == 0 and b_lst[c][r-1] != 0 and b_lst[c-1][r] != 0: # 우로 이동
            b_lst[c][r] = n
            r += 1
            n += 1
        elif b_lst[c][r+1] != 0 and b_lst[c+1][r] == 0: # 하로 이동
            b_lst[c][r] = n
            c += 1
            n += 1
        elif b_lst[c][r - 1] == 0: # 좌로 이동
            b_lst[c][r] = n
            r -= 1
            n += 1
        elif b_lst[c][r - 1] != 0 :# 상으로 이동
            b_lst[c][r] = n
            c -= 1
            n += 1
        # elif b_lst[c][r - 1] != 0 and b_lst[c-1][r] != 0:
        #
        #     b_lst[c][r] = n
        #     c -= 1
        #     n += 1
    print(f'#{T+1}')
    for i in range(1,N+1):
        for j in range(1,N+1):
            print(b_lst[i][j],end = ' ')
        print()
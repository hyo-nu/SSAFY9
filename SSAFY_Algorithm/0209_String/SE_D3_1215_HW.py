# 두 번
Test = 10


# Test = 10
def bf_for(lst, N):  # 8,4
    cnt = 0
    for i in range(len(lst) - N + 1):  # 0 1 2 3 4
        for j in range(N // 2):  # 0 1
            if lst[i + j] != lst[i + N - j - 1]: break
        else:
            cnt += 1
    return cnt


for T in range(Test):
    N = int(input())
    words_row = [input() for _ in range(8)]
    words_col = list(map(list, zip(*words_row)))
    cnt = 0
    for i in range(8):
        cnt += bf_for(words_row[i], N)
        cnt += bf_for(words_col[i], N)

    print(f'#{T + 1}', end=' ')
    print(cnt)


# 처음
def bf_for(total, TL, PL):  # TL  = 10 , PL = 6
    cnt = 0
    for i in range(TL - PL + 1):
        for j in range(PL // 2):
            if total[i + j] != total[PL + i - j - 1]:
                break
        else:
            cnt += 1
    return cnt


Test = 10

for T in range(Test):
    PL = int(input())
    TL = 8
    # 가로를 확인할 배열 생성
    board_row = [input() for _ in range(TL)]

    # 세로를 확인할 배열 생성
    board_column = []
    for i in range(TL):
        board_column.append([board_row[j][i] for j in range(TL)])

    row_cnt, column_cnt = 0, 0
    for j in range(TL):
        row_cnt += bf_for(board_row[j], TL, PL)
        column_cnt += bf_for(board_column[j], TL, PL)
    print(f'#{T + 1}', row_cnt + column_cnt)
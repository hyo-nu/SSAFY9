# 두번
Test = int(input())
# Test = 10

for T in range(Test):
    sdoku = [list(map(int,input().split())) for _ in range(9)]


    count = 0
    # 가로, 세로 확인
    for i in range(9):
        row_sum = 0
        col_sum = 0
        for j in range(9):
            row_sum += sdoku[i][j]
            col_sum += sdoku[j][i]
        if row_sum == 45 : count += 1
        if col_sum == 45 : count += 1
    # 박스 확인

    for i in [0,3,6]:
        for j in [0,3,6]:
            box_sum = 0
            for r in range(3):
                for c in range(3):
                    box_sum += sdoku[r+i][c+j]
            if box_sum == 45 : count += 1

    print(f'#{T + 1}',end = ' ')
    if count == 27 : print(1)
    else : print(0)
# 처음
def sums(arr):
    result = 0
    for i in arr:
        result += i
    return result

def sdoku_check(arr_row):
    count = 0
    # 가로 확인
    for lst1 in arr_row:
        if sums(lst1) == 45 : count += 1

    # 세로 확인
    arr_column =[]
    for j in range(9):
        arr_column.append([arr_row[i][j] for i in range(9)]) # 전치행렬
    for lst2 in arr_column:
        if sums(lst2) == 45 : count += 1

    # box확인
    box_lst =[]
    for k in [0, 3, 6]:
        for l in [0, 3, 6]:
            box_lst = []
            for m in range(3):
                for o in range(3):
                    box_lst += [arr_row[m+k][o+l]]
            if sums(box_lst) == 45 : count += 1
    if count == 27 : return 1
    else : return 0


Test = int(input())

for T in range(Test):
    sdoku = [list(map(int, input().split())) for _ in range(9)] # 스도쿠 한판

    print(f'#{T+1}' ,sdoku_check(sdoku))
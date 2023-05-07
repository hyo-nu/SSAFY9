def eat(arr):
    Max = 0
    for r in range(N): # 0 1 2
        for c in range(N-1): # 1 2
            if arr[r][c] != arr[r][c+1]:
                arr[r][c],arr[r][c+1] = arr[r][c+1],arr[r][c]
                # 가로줄 체크
                for i in range(N):
                    cnt = 1
                    for j in range(N-1):
                        if arr[r][j] == arr[r][j+1] : cnt += 1
                        else : cnt = 1
                    if Max < cnt : Max = cnt

                # 세로줄 체크
                for j in range(N):
                    cnt = 1
                    for i in range(N-1):
                        if arr[i][j] == arr[i+1][j] : cnt += 1
                        else : cnt = 1
                    if Max < cnt: Max = cnt
                arr[r][c], arr[r][c + 1] = arr[r][c + 1], arr[r][c]

    return Max

import sys ; sys.stdin = open('input.txt')
N = int(input())
candy_row = [list(input()) for _ in range(N)]
candy_col = list(map(list,zip(*candy_row)))

print(max(eat(candy_row),eat(candy_col)))
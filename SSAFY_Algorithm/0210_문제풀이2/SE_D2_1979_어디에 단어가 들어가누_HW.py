# 어디에 단어가 들어갈 수 있을까?
import sys

sys.stdin = open("input.txt", "r")

def count(arr, N, K):
    result = 0
    for lst in arr: # 2차원 배열에서 한 행씩 리스트로 반환
        cnt = 0
        for i in range(N):
            if lst[i] == 1 : cnt += 1 # 리스트 요소가 1이면 cnt 세기
            else:
                if cnt == K : result += 1 # 요소가 1 아닐 때, cnt가 K면 단어가 들어갈 수 있음
                cnt = 0 # 대신 공간의 연속이 끊겼으므로 cnt 0으로
        if cnt == K: result += 1 # 한 리스트 요소 체크가 끝났을 때 cnt가 k면 단어가 들어갈 수 있음
    return result

Test = int(input())
for T in range(Test):
    N, K = map(int, input().split())
    puzzle_row = [list(map(int, input().split())) for _ in range(N)]  # 가로 확인을 위한 배열
    puzzle_column = list(map(list, zip(*puzzle_row)))  # 세로 확인을 위한 배열

    row_cnt = count(puzzle_row, N, K)
    column_cnt = count(puzzle_column, N, K)
    print(f'#{T + 1}', row_cnt + column_cnt)

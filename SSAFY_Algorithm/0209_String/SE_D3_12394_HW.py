# 둘
Test = int(input())
# Test = 10
def palindrome(arr,N,M):

    # 가로 회문 확인
    for lst in arr:
        for i in range(N-M+1): # 0,1,2,3,4
            for j in range(M//2): # (012345) , (456789)
                if lst[i+j] != lst[i+M-1-j]: # (i+j) = 시작위치 , (i+M+1-j) = 현위치 + 5 -j
                    break
            else:
                return lst[i:i+M]

    # 전치행렬
    for i in range(N):
        for j in range(N):
            if i < j : arr[i][j], arr[j][i] = arr[j][i], arr[i][j]

    # 세로 회문 확인
    for lst in arr:
        for i in range(N-M+1): # 0,1,2,3,4
            for j in range(M//2): # (012345) , (456789)
                if lst[i+j] != lst[i+M-1-j]: # (i+j) = 시작위치 , (i+M+1-j) = 현위치 + 5 -j
                    break
            else:
                return lst[i:i+M]

# 처음
def bf_for(total, TL, PL):  # TL  = 10 , PL = 6
    for i in range(TL - PL + 1):
        for j in range(PL // 2):
            if total[i + j] != total[PL + i - j - 1]:
                break
        else:
            return total[i:i + PL]


def bf_for(total, TL, PL):  # TL  = 10 , PL = 6
    for i in range(TL - PL + 1):
        for j in range(PL // 2):
            if total[i + j] != total[PL + i - j - 1]:
                break
        else:
            return total[i:i + PL]


Test = int(input())

for T in range(Test):
    N, M = map(int, input().split())
    # 가로를 확인할 배열 생성
    row_arr = [input() for _ in range(N)]
    # 세로를 확인할 배열 생성
    column_arr = list(map(list,zip(*row_arr)))

    for k in range(N):
        if bf_for(row_arr[k], N, M) is not None:
            result = bf_for(row_arr[k], N, M)
        elif bf_for(column_arr[k], N, M) is not None:
            result = bf_for(column_arr[k], N, M)

    print(f'#{T + 1}', ''.join(result))
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


for T in range(Test):

    N, M = map(int,input().split()) # N = 10 , M = 6
    arr = [list(input()) for _ in range(N)]

    result = palindrome(arr,N,M)
    print(f'#{T + 1}',''.join(result))

# 처음

Test = int(input())

for T in range(Test):
    # N NxN 행렬
    # M 확인할 문자의 길이
    N,M = map(int,input().split())
    word_arr2 = [[0]*N for _ in range(N)]
    for c in range(N):

        # 가로줄 회문인지 확인
        # N = 20
        # M = 13
        # 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19
        # E C F Q B K S Y B B  O  S  Z  Q  S  F  B  X  K  I
        word = list(input())
        for i in range(0,N-M+1): # 0 1 2 3 4 5 6 7
            count = 0
            for j in range(0, M // 2): # 0 1 2 3 4 5
                if word[i + j] == word[M + i -j -1]: # i = 1 일때 1 13,2 12
                    count += 1                       # i = 2 일때 2 14,3 13
                # print(f'{c+1}문자{i}번째시작{j+1}번 문자 : ', count)
            if count == M // 2:
                print(f'#{T+1}', ''.join(word[i:i+M]))
                break # 회문이 맞으면은 for_in 나가기
        # 세로행렬을 가로로 만들기
        if count == M // 2:
            break
        for r in range(N):
            word_arr2[r][c] = word[r]
    else:
    # print(word_arr2)
    # 세로줄 회문인지 확인 (가로줄이 회문이 아니였으므로)
        for c in range(N):
            for i in range(0, N - M + 1):  # 0 1 2 3 4 5 6 7
                count = 0
                for j in range(0, M // 2):  # 0 1 2 3 4 5
                    if word_arr2[c][i + j] == word_arr2[c][M + i - j - 1]:  # i = 1 일때 1 13,2 12
                        count += 1  # i = 2 일때 2 14,3 13
                # print(f'{c}열의{i}번째에서 시작 : ',count)
                if count == M // 2:
                    print(f'#{T + 1}', ''.join(word_arr2[c][i:i+M]))
                    break  # 회문이 맞으면은 for_in 나가기
            if count == M // 2:
                break
    # for c in range(N):
    #     print(*word_arr2[c])
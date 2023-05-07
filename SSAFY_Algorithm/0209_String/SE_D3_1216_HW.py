
#두번
Test = 10
# Test = 10
def bf_for(lst,RC): # 8,4
    for rc in range(RC,0,-1):
        for i in range(len(lst)-rc+1): # 0 1 2 3 4
            for j in range(rc//2): # 0 1
                if lst[i+j] != lst[i+rc-j-1] : break
            else : return rc

for T in range(Test):
    TC = int(input())
    RC = 100
    words_row = [input() for _ in range(RC)]
    words_col = list(map(list,zip(*words_row)))

    Max = 0
    for i in range(RC):
        if Max < max(bf_for(words_row[i],RC),bf_for(words_col[i],RC)):
            Max = max(bf_for(words_row[i], RC), bf_for(words_col[i], RC))
    print(f'#{T + 1}',end = ' ')
    print(Max)

#처음
# 배열을 받아서 회문의 최대 길이 m을 반환 하는 함수
def palindrome(arr, N, M):
    max_value = 0
    m_value = 0
    for m in range(M, 1, -1):
        for lst in arr:
            for i in range(N - m + 1):  # 전체길이 - 회문의길이 + 1 = 회문의 시작위치들
                for j in range(m // 2):  # 양끝을 가운데로 이동하며 확인, so 회문 길이의 절반
                    if lst[i + j] != lst[m + i - j - 1]:
                        break
                else:
                    m_value = m
                    break
        if max_value <= m_value : max_value = m_value
    return max_value


Test = 10

for T in range(Test):
    Test_case = int(input())
    N, M = 100, 100

    row = [input() for _ in range(N)]  # 가로 검증 배열
    column = list(map(list, zip(*row)))  # 세로 검증 배열

    if palindrome(column, N, M) <= palindrome(row, N, M):
        print(f'#{Test_case}', palindrome(row, N, M))
    else : print(f'#{Test_case}', palindrome(column, N, M))

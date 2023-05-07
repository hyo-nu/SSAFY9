
# 둘째
def palindrome(A,B,a,b):
    i = j = cnt = 0

    while i < a:
        if A[i] == B[j]:
            i += 1
            j += 1
            if j == b:
                cnt += 1
                j = 0
        else:
            i = i - j + 1
            j = 0

    return cnt
Test = int(input())
# Test = 10

for T in range(Test):
    A,B = input().split()
    a = len(A)
    b = len(B)
    result = a + palindrome(A,B,a,b)- (b * palindrome(A,B,a,b))

    print(f'#{T + 1}',result)


# 처음
def bf_while(A,B,N,M):
    i = 0
    j = 0
    cnt = 0
    while i < N :
        if A[i] == B[j]:
            i += 1
            j += 1
            if j == M:
                j = 0
                cnt += 1
        else:
            i = i - j + 1
            j = 0
    return cnt
Test = int(input())

for T in range(Test):
    A,B = input().split()
    N = len(A) # 전체 테스트
    M = len(B) # 패턴

    pattern_cnt = bf_while(A, B, N, M)
    key_min = N + pattern_cnt - (pattern_cnt * M)
    print(f'#{T+1}',key_min)
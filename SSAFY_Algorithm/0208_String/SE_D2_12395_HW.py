
# 두번째
Test = int(input())
# Test = 10

for T in range(Test):

    str1 = input()
    str2 = input()

    Max = 0
    for i in str1:
        Sum = 0
        for j in str2:
            if i == j : Sum += 1
        if Max < Sum : Max = Sum

    print(f'#{T + 1}',Max)

# 처음
Test = int(input()) # 입력 : 5

for T in range(Test): # T : 01234
    str1 = input() # 입력 : abca
    str2 = input() # 입력 : ababca
    N = len(str1) # N = 4
    M = len(str2) # M = 6

    max = 0
    for i in str1: # a b c a
        cnt = 0
        for j in str2: # a b a b c a
            if i == j : cnt += 1
        if max < cnt: max = cnt
    print(f'#{T+1}',max)

# 교수님 코드

for T in range(Test): # T : 01234
    str1 = input() # 입력 : abca
    str2 = input() # 입력 : ababca

    # 아스키 코드를 다양하게 이용할 수 있겠누!!!
    # 메모리를 추가적으로 사용해서 쉽게 작성
    cnt = [0] * 128 # ASCII 코드값을 배열의 인덱스로 사용

    for ch in str2:
        cnt[ ord(ch) ] += 1

    ans = 0
    for ch in str1:
        if ans < cnt[ ord(ch) ]:
            ans = cnt[ord(ch)]
    print(ans)
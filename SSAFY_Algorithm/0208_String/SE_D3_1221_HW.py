
# 둘째
Test = int(input())
# Test = 10
word = ["ZRO", "ONE", "TWO", "THR", "FOR", "FIV", "SIX", "SVN", "EGT", "NIN"]

for T in range(Test):

    TC,N = input().split()
    nums = list(input().split())
    cnt_lst = [0] * len(word)

    for i in range(len(word)):
        for j in nums:
            if word[i] == j : cnt_lst[i] += 1

    print(f'#{T + 1}')
    for i in range(len(cnt_lst)):
        for j in range(cnt_lst[i]) : print(word[i],end=' ')

# 처음
Test = int(input())
nums = ["ZRO", "ONE", "TWO", "THR", "FOR", "FIV", "SIX", "SVN", "EGT", "NIN"]

for T in range(Test):
    T_num , T_len = input().split()
    Testcase = list(map(str,input().split()))

    cnt = [0]*10
    for i in range(len(nums)):
        for j in Testcase:
            if nums[i] == j: cnt[i] += 1
    print(f'#{T+1}')

    for j in range(len(nums)): # 0 1 2 3 4 5 6 7 8 9
        for _ in range(cnt[j]):
            print(nums[j],end = ' ')
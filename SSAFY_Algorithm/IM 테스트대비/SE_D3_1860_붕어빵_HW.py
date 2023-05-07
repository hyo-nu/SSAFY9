# 붕어빵
def Possible():
    bread = 0
    if nums[0] >= M:
        for n in range(1, ((nums[-1] // M) + 1)):
            people = 0
            bread += K
            for i in nums:
                if M * n <= i < M * n + M:
                    people += 1
                    if people > bread : return False
                elif i >= M * n + M :
                    bread -= people
                    break
    else :
        return False
    return True

def New_Possible():
    people = 0
    for i in nums:
            people += 1
            if people > (i // M) * K:
                return False
    else:
        return True

Test = int(input())

for T in range(Test):
    # N : 사람수, M : M초동안 , K : K개 붕어빵 제작
    N, M, K = map(int, input().split())
    nums = list(map(int, input().split()))
    nums.sort()

    print(f'#{T + 1}', end=' ')
    if Possible():
        print('Possible')
    else:
        print('Impossible')

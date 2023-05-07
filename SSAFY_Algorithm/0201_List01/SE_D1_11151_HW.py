Test = int(input())

for T in range(Test):
    N = int(input())
    nums = list(map(int, input().split()))

    # 인접한 두 수의 합을 list comprehesion으로 간단히 표현함
    sum_lst = [nums[i] + nums[i + 1] for i in range(N - 1)]

    Max = -400
    for i in range(len(sum_lst)):
        if Max < sum_lst[i]: Max = sum_lst[i]
    print(f'#{T + 1}', Max)

# 첫번째 풀이
Test = int(input())

for T in range(Test):
    N = int(input())
    N_lst = list(map(int, input().split()))

    # 두수의 합 list를 제작

    sum_max = -400
    for i in range(N - 1):
        # 두수의 합의 max값
        sum = N_lst[i] + N_lst[i + 1]
        if sum_max < sum:
            sum_max = sum

    print(f'#{T + 1} {sum_max}')
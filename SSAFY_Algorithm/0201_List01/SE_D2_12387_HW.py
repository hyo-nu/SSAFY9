# 세번째 풀이
Test = int(input())

for T in range(Test):
    N, M = map(int, input().split())
    nums = list(map(int, input().split()))
    n_sum = []  # 구간합을 담을 리스트
    n_sum.append(nums[0] + nums[1] + nums[2])  # 구간합 처음값

    # 구간합의 처음을 빼고 맨뒤에 값 추가
    for i in range(N - M):  # 0 1 2 3 4 5 6
        n_sum.append(n_sum[i] - nums[i] + nums[i + M])

    # 버블 정렬
    for j in range(len(n_sum) - 1, 0, -1):
        for k in range(j):
            if n_sum[k] > n_sum[k + 1]:
                n_sum[k], n_sum[k + 1] = n_sum[k + 1], n_sum[k]
    print(f'#{T + 1}', n_sum[-1] - n_sum[0])

# 두번째 풀이
Test = int(input())

for T in range(Test):
    N, M = map(int, input().split())
    N_lst = list(map(int, input().split()))

    max = 0
    min = 10000 ** 3
    for n in range(N - M + 1):  # 0,1,2,3,4,5,6,7
        m_sum = 0
        for m in range(M):
            m_sum += N_lst[n + m]
        if max < m_sum:
            max = m_sum
        if min > m_sum:
            min = m_sum

    print(f'#{T + 1} {max - min}')

# 처음 풀이
Test = int(input())

for T in range(Test):
    N, M = map(int, input().split())
    v = list(map(int, input().split()))

    sum_lst = []
    for i in range(N - M + 1):
        sum = 0
        for j in range(M):
            sum += v[i + j]
        sum_lst.append(sum)

    max_sum = sum_lst[0]
    min_sum = sum_lst[0]

    for i in range(1, N - M + 1):
        if max_sum < sum_lst[i]:
            max_sum = sum_lst[i]

        if min_sum > sum_lst[i]:
            min_sum = sum_lst[i]

    print(f'#{T + 1} {max_sum - min_sum}')
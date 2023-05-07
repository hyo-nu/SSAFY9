# 선택정렬
Test = int(input())

for T in range(Test):
    N = int(input())
    nums = list(map(int, input().split()))

    for i in range(N - 1):  # 0 1 2 3
        Minidx = i
        for j in range(i + 1, N):
            if nums[Minidx] > nums[j]:
                Minidx = j
        nums[i], nums[Minidx] = nums[Minidx], nums[i]

    print(f'#{T + 1}', *nums)
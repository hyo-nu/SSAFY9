# 두번쨰 풀이

Test = int(input())

for T in range(Test):
    N = int(input())
    nums = list(map(int,input().split()))

    Max = 0
    Min = 1000001

    for i in range(N):
        if Max < nums[i] : Max = nums[i]
        if Min > nums[i] : Min = nums[i]

    print(f'#{T+1}',Max-Min)

# 첫 풀이
Test = int(input())

for T in range(Test):
    N = int(input())
    a = list(map(int, input().split()))

    a_min = a[0]
    a_max = a[0]

    for i in range(1,N):
        if a_max < a[i]:
            a_max = a[i]

        if a_min > a[i]:
            a_min = a[i]

    print(f'#{T+1} {a_max-a_min}')
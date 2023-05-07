# 두번째
# Test = int(input())
Test = 10

for T in range(Test):
    N = int(input())
    buildings = list(map(int, input().split()))

    sun_buliding = 0
    for i in range(2, N - 2):
        high_building = 0
        for j in range(i - 2, i + 3):
            if j != i and high_building < buildings[j]:
                high_building = buildings[j]
        if buildings[i] > high_building:
            sun_buliding += buildings[i] - high_building

    print(f'#{T + 1}', sun_buliding)

# 첫번째
Test = 10

for T in range(Test):
    bulid_N = int(input())
    build_lst = list(map(int, input().split()))
    sum = 0

    for i in range(2, bulid_N - 2):
        max = 0
        for j in range(i - 2, i + 3):
            if i != j:
                if max < build_lst[j]: max = build_lst[j]
        if build_lst[i] > max:
            sum += build_lst[i] - max

    print(f'#{T + 1} {sum}')
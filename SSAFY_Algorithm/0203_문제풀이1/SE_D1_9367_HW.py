# 두번째
Test = int(input())
# Test = 10

for T in range(Test):
    N = int(input())
    carrot = list(map(int, input().split()))

    cnt = Max = 0

    for c in range(len(carrot) - 1):
        if carrot[c] < carrot[c + 1]:
            cnt += 1
            if Max < cnt: Max = cnt
        else:
            cnt = 0

    print(f'#{T + 1}', Max + 1)

# 첫번째
Test = int(input())

for T in range(1, Test + 1):
    N = int(input())
    numbers = list(map(int, input().split()))
    ans = cnt = 0

    for i in range(len(numbers) - 1):
        if numbers[i + 1] - numbers[i] != 1:
            cnt = 0
        elif numbers[i + 1] - numbers[i] == 1:
            cnt += 1
            if ans < cnt:
                ans = cnt

    print(f'#{T}', ans + 1)

# 두번째
Test = int(input())
# Test = 10

for T in range(Test):
    N = int(input())
    lst = input().split('0')

    Max = 0
    for i in lst:
        cnt = 0
        for j in i:
            cnt += 1
        if Max < cnt:
            Max = cnt
    print(f'#{T+1}',Max)

# 첫번째
Test = int(input())

for T in range(1,Test+1):
    N = int(input())
    numbers = list(map(int,input()))
    ans = cnt = 0

    for i in numbers:
        if i == 0 :
            cnt = 0
        elif i == 1 :
            cnt += 1
            if ans <cnt:
                ans = cnt

    print(f'#{T}',ans)
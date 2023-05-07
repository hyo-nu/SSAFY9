# 두번쨰 풀이
Test = int(input())
# Test = 10

for T in range(Test):
    N = int(input())

    lst = [0] * 5001
    for i in range(N):
        A, B = map(int, input().split())
        for i in range(A, B + 1):
            lst[i] += 1

    p = int(input())

    lst_a = []
    for i in range(p):
        c = int(input())
        lst_a.append(lst[c])

    print(f'#{T + 1}', *lst_a)
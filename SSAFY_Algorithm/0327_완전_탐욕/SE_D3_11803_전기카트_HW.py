def perm(i, k):
    if i == k:
        lst = [1] + [*p] + [1]
        Sum = 0
        for i in range(len(lst) - 1):
            Sum += arr[lst[i] - 1][lst[i + 1] - 1]
        if min(Min) > Sum: Min.append(Sum)

    else:
        for j in range(i, k):
            p[i], p[j] = p[j], p[i]
            perm(i + 1, k)
            p[i], p[j] = p[j], p[i]


Test = int(input())

for TC in range(Test):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    p = [i for i in range(2, N + 1)]
    Min = [(N ** 2) * 100]
    perm(0, N - 1)

    print(f'#{TC + 1}', Min[-1])

#================================================
# 교수님의 전기카트
def perm(k):
    global ans
    if k == N:
        cost = 0
        for i in range(1, N):
            cost += G[order[i-1]][order[i]]
        cost += G[order[N-1]][0]
        if ans > cost:
            ans = cost
    else:
        for i in range(k, N):
            order[k], order[i] = order[i], order[k]
            perm(k + 1)
            order[k], order[i] = order[i], order[k]

for tc in range(1, int(input()) + 1):
    N = int(input())   # 정점들 = {0(사무실), 1, 2, 3}
    G = [list(map(int, input().split())) for _ in range(N)]

    order = [i for i in range(N)]

    ans = 0xfffffff
    perm(1)
    print(ans)

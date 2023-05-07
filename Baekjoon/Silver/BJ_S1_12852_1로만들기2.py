N = int(input())
DP = [0] * (N + 1)
vi = [[] for _ in range(N+1)]
vi[1].append([1])

for i in range(2, N + 1):
    DP[i] = DP[i - 1] + 1
    for j in range(len(vi[i-1])):
        vi[i] += [vi[i-1][j] + [i]]

    if i % 2 == 0 :
        DP[i] = min(DP[i], DP[i//2] + 1)
        if DP[i] == DP[i//2] + 1:
            vi[i].clear()
            for j in range(len(vi[i//2])):
                vi[i] += [vi[i//2][j] + [i]]
    if i % 3 == 0 :
        DP[i] = min(DP[i], DP[i//3] + 1)
        if DP[i] == DP[i//3] + 1:
            vi[i].clear()
            for j in range(len(vi[i//3])):
                vi[i] += [vi[i // 3][j] + [i]]

print(DP[N])
print(*sorted(*vi[N],reverse=True))

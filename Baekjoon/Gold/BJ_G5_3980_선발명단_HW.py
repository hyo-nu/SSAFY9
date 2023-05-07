# i번 선수, j번 포지션
# 적합한 포지션 수는 최대 5개

def DFS(n,Sum):
    if n == N:
        ans.append(Sum)
        return
    for i in range(N):
        if S[i][n] != 0 and v[i] == 0:
            v[i] = 1
            DFS(n + 1,Sum + S[i][n])
            v[i] = 0

Test = int(input())

for T in range(Test):
    N = 3
    S = [list(map(int, input().split())) for _ in range(N)]
    ans, v = [], [0] * N
    DFS(0,0)
    ans.sort()
    print(ans[-1])


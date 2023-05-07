import sys;sys.stdin=open('input.txt')

def back(r,mul):
    global Max
    if Max >= mul:return
    if r == N:
        if Max < mul:
            Max = mul
        return
    for c in range(N):
        if used[c] : continue
        used[c] = 1
        back(r+1,mul*P[r][c]/100)
        used[c] = 0

Test = int(input())

for TC in range(Test):
    N = int(input())
    P = [list(map(int,input().split())) for _ in range(N)]
    Max = 0
    used = [0] * N
    back(0,1)
    print(f'#{TC+1} {Max*100:.6f}')


#===================================
# 교수님
for tc in range(1, int(input()) + 1):
    N = int(input())
    P = [list(map(lambda x: float(x) / 100, input().split())) for _ in range(N)]

    memo = [[0] * (1 << N) for _ in range(N + 1)]

    def find_max(n, visit):
        if n == N:
            return 1
        if memo[n][visit]:
            return memo[n][visit]
        else:
            for i in range(N):
                if visit & (1 << i): continue
                memo[n][visit] = max(memo[n][visit], find_max(n + 1, visit | (1 << i)) * P[n][i])
        return memo[n][visit]


    ans = find_max(0, 0)

    print(f'#{tc} {ans * 100:.6f}')

#===================================================
# 문어박사님 코드
def DFS(n,bits):
    if n == N:
        return 1
    if memo[bits] == 0 : # 호출된적 없음 -> 계산 후 최대값 저장해 두면 부를 일이 없음
        mx = 0
        for j in range(N):
            if bits & (1<<j) == 0: # 미방문임
                mx = max(mx, DFS(n+1, bits+(1<<j)) * P[n][j]/100)
        memo[bits] = mx

    return memo(bits)

for tc in range(1, int(input()) + 1):
    N = int(input())
    P = [list(map(lambda x: float(x) / 100, input().split())) for _ in range(N)]

    memo = [0] * (2 ** N)
    ans = DFS(0,0)*100

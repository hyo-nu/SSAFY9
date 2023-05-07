# 4 <= N <= 16
# 1 <= S <= 20,000
import sys;sys.stdin=open('input.txt')

def comb(n, stop):
    if stop == 0:
        A = []
        B = []
        A_taste = B_taste = 0
        for i in range(N):
            if i in lst : A.append(i)
            else : B.append(i)

        for i in range(N//2):
            A_taste +=

        return

    for j in range(n,N - stop + 1):
        if not used[j]:
            used[j] = 1
            lst.append(j)
            comb(n+1,stop-1)
            lst.pop()
            used[j] = 0

Test = int(input())

for TC in range(Test):
    N = int(input())
    G = [list(map(int,input().split())) for _ in range(N)]
    lst = []
    used = [0] * (N + 1)
    comb(0,N//2)

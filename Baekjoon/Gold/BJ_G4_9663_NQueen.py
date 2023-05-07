def checking(r,c):
    for i in range(r):
        if abs(r-i) == abs(cols[i]-c): return False
    return True

def nQueen(n):
    global ans
    if n == N:
        ans += 1
        return

    for i in range(N):
        if used[i] : continue
        if not checking(n,i) : continue
        used[i] = 1
        cols[n] = i
        nQueen(n+1)
        used[i] = 0

N = int(input())
used = [0] * (N + 1)
cols = [0] * (N + 1)
ans = 0
nQueen(0)
print(ans)

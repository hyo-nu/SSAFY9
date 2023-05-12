import sys;sys.stdin=open('input.txt')

N = int(input())
lst = list(map(int,input().split()))
S = []

for i in range(N-1,-1,-1):
    while S:
        if lst[i] >= S[-1]: S.pop()
        elif lst[i] < S[-1]:
            tmp = lst[i]
            lst[i] = S[-1]
            S.append(tmp)
            break
    if not S:
        S.append(lst[i])
        lst[i] = -1

print(*lst)



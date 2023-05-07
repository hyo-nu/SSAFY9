import sys;sys.stdin=open('input.txt')

N = int(input())
S = []
for _ in range(N):
    lst = list(input().split())
    if lst[0] == 'push':
        S.append(lst[1])
    elif lst[0] == 'pop':
        if S : print(S.pop())
        else : print(-1)
    elif lst[0] == 'size':
        print(len(S))
    elif lst[0] == 'empty':
        if S : print(0)
        else : print(1)
    elif lst[0] == 'top':
        if S : print(S[-1])
        else : print(-1)
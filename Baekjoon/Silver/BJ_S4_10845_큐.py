import sys;sys.stdin=open('input.txt')
input = sys.stdin.readline

N = int(input())
Q = []
for _ in range(N):
    lst = list(input().split())
    if lst[0] == 'push' : Q.append(lst[1])
    elif lst[0] == 'pop' :
        if Q : print(Q.pop(0))
        else : print(-1)
    elif lst[0] == 'size' : print(len(Q))
    elif lst[0] == 'empty' :
        if Q : print(0)
        else : print(1)
    elif lst[0] == 'front' :
        if Q : print(Q[0])
        else : print(-1)
    elif lst[0] == 'back':
        if Q : print(Q[-1])
        else : print(-1)

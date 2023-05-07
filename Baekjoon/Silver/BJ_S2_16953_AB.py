import sys;sys.stdin=open('input.txt')

def back(n,A):
    global Min
    if Min <= n : return
    if A == B:
        Min = min(Min,n)
        return
    if len(str(A)) > len(str(B)) : return
    back(n+1,A*2)
    back(n+1,int(str(A)+'1'))

A,B = map(int,input().split())
Min = 0xffffffffffffffff
back(1,A)
if Min == 0xffffffffffffffff : print(-1)
else : print(Min)
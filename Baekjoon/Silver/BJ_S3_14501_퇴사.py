import sys;sys.stdin=open('input.txt')

def back(date,revenue):
    global Max
    if date == N:
        Max = max(Max,revenue)
        return
    if date > N: return
    back(date+lst[date][0],revenue+lst[date][1])
    back(date+1,revenue)

N = int(input())
lst = [list(map(int,input().split())) for _ in range(N)]
Max = 0
back(0,0)
print(Max)
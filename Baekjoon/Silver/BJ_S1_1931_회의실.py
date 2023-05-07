import sys;sys.stdin=open('input.txt')
input = sys.stdin.readline

N = int(input())
conf = [list(map(int,input().split())) for _ in range(N)]
conf.sort(key = lambda x : (x[1],x[0]))

reserve= [[0,-1]]
for ST,ET in conf:
    if reserve[-1][1] <= ST:
        reserve.append([ST,ET])
print(len(reserve)-1)

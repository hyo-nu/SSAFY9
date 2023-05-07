import sys;sys.stdin=open('input.txt')

def comb(start,stop,Sum):
    global Min
    if stop == 0:
        if Sum >= B:
            if Min >= Sum:
                Min = Sum
        return
    for i in range(start,N-stop+1):
        comb(i+1,stop-1,Sum+tall[i])


Test = int(input())

for TC in range(Test):
    N, B = map(int,input().split())
    tall = sorted(list(map(int,input().split())))
    Min = 9999999
    ans = []
    for k in range(1,N+1):
        comb(0,k,0)
    print(f'#{TC+1}',Min-B)
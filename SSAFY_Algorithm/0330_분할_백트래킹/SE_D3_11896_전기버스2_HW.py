import sys ; sys.stdin = open("input.txt")

def move(start, cnt, energy, charge):
    global Min
    if Min <= cnt or energy < 0:
        return
    if start >= N - 1:
        if Min > cnt:
            Min = cnt
        return
    energy = charge
    move(start + 1, cnt + 1, energy - 1, bus[start + 1])
    move(start + 1, cnt, energy - 1, energy - 1)


Test = int(input())

for TC in range(Test):
    N, *bus = list(map(int, input().split()))
    bus = bus + [0]
    Min = N
    move(0, 0, bus[0], bus[0])
    print(f'#{TC + 1}', Min)
#======================================================

Test = int(input())

for TC in range(Test):
    stop = list(map(int, input().split()))
    N = stop[0]

    def find_min(n,battery,cnt):
        global ans
        if ans <= cnt:return
        if n == N:
            ans = min(ans,cnt)
        else:
            find_min(n+1, stop[n]-1,cnt+1)
            if battery > 0:
                find_min(n+1, battery-1,cnt)

    find_min(2,stop[1] - 1, 0)




















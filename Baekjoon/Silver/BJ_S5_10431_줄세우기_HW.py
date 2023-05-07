import sys;sys.stdin = open('input.txt')
Test = int(input())

for TC in range(Test):
    info = list(map(int,input().split()))
    N = info[0]
    height = info[1:]
    cnt = 0

    for i in range(19,0,-1):
        for j in range(i,-1,-1):
            if height[i] < height[j]:
                cnt += 1
    print(N,cnt)
import sys;sys.stdin=open('input.txt')

Test = int(input())

for TC in range(Test):
    N = int(input())
    arr = [list(map(int,input().split())) for _ in range(N)]
    arr.sort(key = lambda x:x[1])
    cnt = time = 0
    for i in range(N):
        s = arr[i][0]
        e = arr[i][1]
        if time <= s:
            cnt += 1
            time = e
    print(f'#{TC+1}', cnt)
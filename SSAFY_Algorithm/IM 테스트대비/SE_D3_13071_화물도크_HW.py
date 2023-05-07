import sys; sys.stdin = open('input.txt')

def func():

    for i in range(1 << len(AP), -1, -1):
        cnt = 0
        for j in range(len(AP)):
            if i & (1 << j):
                cnt += 1
                for c in range(i[0], i[1] + 1):
                    Time[c] += 1
            if 2 not in Time:
                return cnt

Test = int(input())

for T in range(Test):
    N = int(input())
    Time = [0] * 25
    AP = [list(map(int,input().split())) for _ in range(N)]

    print(func())
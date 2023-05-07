# 1 <= N,M <= 50
import sys;sys.stdin=open('input.txt')

Test = int(input())

for TC in range(Test):
    J,N = map(int,input().split())

    box = []
    for _ in range(N):
        R,C = map(int,input().split())
        box.append(R*C)

    Sum = 0
    box.sort(reverse=True)
    for i in range(N):
        Sum += box[i]
        if Sum >= J:
            result = i+1
            break
    print(result)
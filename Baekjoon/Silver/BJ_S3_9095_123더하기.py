import sys;sys.stdin=open('input.txt')

def back(sm):
    global cnt
    if sm > N : return
    elif sm == N :
        cnt += 1
        return
    back(sm+1)
    back(sm+2)
    back(sm+3)

Test = int(input())
for TC in range(Test):
    cnt = 0
    N = int(input())
    back(0)
    print(cnt)
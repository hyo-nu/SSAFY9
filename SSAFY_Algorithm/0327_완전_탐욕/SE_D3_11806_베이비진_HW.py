import sys;sys.stdin = open("input.txt")

def baby_gin(P):
    for i in range(10):
        if P[i] == 3: return True
    for i in range(8):
        if P[i] and P[i+1] and P[i+2]:return True

    return False
Test = int(input())

for TC in range(Test):
    nums = list(map(int,input().split()))
    P1 = [0] * 10
    P2 = [0] * 10
    result = 0
    for num in range(0,12,2):
        P1[nums[num]] += 1
        P2[nums[num+1]] += 1

        if baby_gin(P1):
            result = 1 ; break
        if baby_gin(P2):
            result = 2 ; break

    print(f'#{TC+1}',result)


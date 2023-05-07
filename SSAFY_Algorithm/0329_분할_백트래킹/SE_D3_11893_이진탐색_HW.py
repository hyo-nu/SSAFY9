import sys ; sys.stdin= open('input.txt')

def binarysearch(key):
    global L_cnt, R_cnt
    L = 0
    R = N - 1
    Before_L = Before_R = 0
    while L <= R:
        mid = (L + R) // 2
        if N_lst[mid] == key:
            return 1
        elif N_lst[mid] > key:
            if Before_L == 1: return 0
            Before_R = 0
            Before_L = 1
            R = mid - 1
        else:
            if Before_R == 1: return 0
            Before_R = 1
            Before_L = 0
            L = mid + 1
    return 0

Test = int(input())

for TC in range(Test):
    N, M = map(int,input().split())
    N_lst = sorted(list(map(int,input().split())))
    M_lst = list(map(int,input().split()))
    cnt = 0
    for key in M_lst:
        cnt += binarysearch(key)

    print(f'#{TC+1}',cnt)



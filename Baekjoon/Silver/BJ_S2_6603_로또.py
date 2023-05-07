# 6 < k < 13
from itertools import combinations
import sys;sys.stdin = open('input.txt')

while True:
    K,*S_lst = list(map(int,input().split()))
    if K == 0 : break
    for lst in combinations(S_lst,6):
        print(*lst)
    print()




# import sys;sys.stdin=open('input.txt')
# from heapq import heappop, heappush
# input = sys.stdin.readline
#
# N = int(input())
# h = []
# for _ in range(N):
#     x = int(input())
#     if x > 0 : heappush(h,x)
#     else :
#         if h : print(heappop(h))
#         else : print(0)


# import sys;sys.stdin=open('input.txt')
# from heapq import heappop, heappush
# input = sys.stdin.readline
#
# N = int(input())
# h = []
# for _ in range(N):
#     x = int(input())
#     if x > 0 : heappush(h,-x)
#     else :
#         if h : print(-heappop(h))
#         else : print(0)


import sys;sys.stdin=open('input.txt')
from heapq import heappop, heappush
input = sys.stdin.readline

N = int(input())
h = []
for _ in range(N):
    x = int(input())
    if x != 0 : heappush(h,(abs(x),x))
    else :
        if h : print(heappop(h)[1])
        else : print(0)
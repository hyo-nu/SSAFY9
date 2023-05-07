import sys;sys.stdin=open('input.txt')
# from itertools import combinations
#
# Test = int(input())
#
# for TC in range(Test):
#     # 1 <= N <= 20
#     # 1 <= cal <= 10,000
#     # 1 <= info <= 1,000
#     N,kal = map(int,input().split())
#     info = [list(map(int,input().split())) for _ in range(N)]
#
#     Max = 0
#     for i in range(1,N+1):
#         menu = list(combinations(info,i))
#
#         for lst in menu:
#             score = kal_sum = 0
#
#             for T,K in lst:
#                 score += T
#                 kal_sum += K
#
#             if kal_sum <= kal:
#                 if Max < score:
#                     Max = score
#     print(f'#{TC+1}',Max)
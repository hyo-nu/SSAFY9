# import sys;sys.stdin = open("input.txt")
#
# Test = int(input())
#
# for TC in range(Test):
#     num, ch = map(int,input().split())
#     num = list(map(int,str(num)))
#     N = len(num)
#     posi = -1
#
#     for _ in range(ch):
#         Max_id = N - 1
#         for i in range(N-2,posi,-1):
#             if num[Max_id] < num[i]:
#                 Max_id = i
#
#         posi += 1
#         if posi == N-1 : posi -= 1
#         num[posi], num[Max_id] = num[Max_id], num[posi]
#
#     print(f'#{TC+1}',''.join(map(str,num)))

#===============================================



# N = int(input())
# N_lst = list(map(int,input().split()))
# DP_P = [0] * 100000001
# DP_M = [0] * 100000001
#
# for n in N_lst :
#     if n >= 0 : DP_P[n] = 1
#     else : DP_M[-n] = 1
#
# for i,n in enumerate(N_lst) :
#     sm = 0
#     if n >= 0 :
#         sm += sum(DP_P[:n])
#         sm += sum(DP_M)
#     else:
#         sm += sum(DP_M[-(n-1):])
#     N_lst[i] = sm
# print(*N_lst)
import sys;sys.stdin=open('input.txt')

N = int(input())
N_lst = list(map(int,input().split()))
lst = sorted(list(N_lst))
dic = {lst[i] : i for i in range(len(lst))}
for i in range(N):
    print(dic[N_lst[i]],end=' ')

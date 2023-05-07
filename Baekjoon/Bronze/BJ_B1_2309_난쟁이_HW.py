# import time
# start = time.time()
#
# def back(n,lst,sum):
#     if n > 8:
#         if len(lst) == 7 and sum == 100:
#             ans.append(lst)
#         return
#     if sum > 100 :
#         return
#     back(n+1,lst + [seven[n]],sum + seven[n])
#     back(n+1,lst,sum)
#
# seven = [int(input()) for _ in range(9)]
# ans =[]
# back(0,[],0)
#
# result = sorted(ans[0])
#
# for i in result:
#     print(i)
# print("time:",time.time()- start)

#문어 박사님
#===============================================
# def solve():
#     N = 9
#     num = sum(lst) - 100
#     for i in range(N-1):
#         for j in range(i+1,N): # N개중에 2개를 뽑는 경우
#             if lst[i] + lst[j] == num:
#                 return lst[i], lst[j]
#
# lst = [int(input()) for _ in range(9)]
# n, m = solve()   # 7명에 포한되지 않는 2명 찾기
# for i in sorted(lst):
#     if i !=n and i!=m:
#         print(i)

#====================================================





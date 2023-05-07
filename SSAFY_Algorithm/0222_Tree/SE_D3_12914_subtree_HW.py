# def inorder(N):
#     global cnt
#     if not G[N]:
#         return
#
#     for w in G[N]:
#         if node[w] == 0:
#             node[w] = 1
#             inorder(w)
#             cnt += node[w]
#
# Test = int(input())
#
# for T in range(Test):
#     E, N = map(int,input().split())
#     E_lst = list(map(int,input().split()))
#     G = [[]for _ in range(E+2)]
#     node = [0] * (E+2)
#
#     for i in range(0,E*2,2):
#         u,v = E_lst[i],E_lst[i+1]
#         G[u].append(v)
#
#     cnt = 1
#     node[N] = 1
#     inorder(N)
#     print(f'#{T+1}',cnt)

def subtree(N):
    if N == 0:
        return
    global cnt
    cnt += 1
    subtree(L[N])
    subtree(R[N])

import sys ; sys.stdin = open('input.txt')

Test = int(input())

for T in range(Test):
    E,N = map(int,input().split())
    Edge = list(map(int, input().split()))
    L = [0] * (E + 2)
    R = [0] * (E + 2)
    P = [0] * (E + 2)

    for i in range(0,E*2,2):
        p, c = Edge[i] , Edge[i+1]
        if L[p] == 0:
            L[p] = c
        else:
            R[p] = c
    cnt = 0
    subtree(N)
    print(f'#{T+1}',cnt)


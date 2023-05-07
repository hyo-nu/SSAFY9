# def inorder(ver):
#     global word
#     if ver == 0:
#         return
#
#     inorder(int(L[ver]))
#     word += node[ver]
#     inorder(int(R[ver]))
#
# Test = 10
#
# for T in range(Test):
#     N = int(input())
#     L = [0] * (N + 1)
#     R = [0] * (N + 1)
#     P = [0] * (N + 1)
#
#     node = [0] * (N + 1)
#     for i in range(1, N + 1):
#         v = list(input().split())
#         node[i] = v[1]  # 각 정점의 요소
#
#         if len(v) >= 3: L[i], P[int(v[2])] = v[2], i  # 부모, 좌정점 = 좌정점, 부모
#         if len(v) >= 4: R[i], P[int(v[3])] = v[3], i  # 부모, 우정점 = 우정점, 부모
#
#     word = ''
#     inorder(1)
#     print(f'#{T+1}',word)
import sys ; sys.stdin = open('input.txt')

def subtree(v):
    if v == 0:
        return

    global word
    subtree(L[v])
    word += P[v]
    subtree(R[v])

Test = 10

for T in range(Test):
    N = int(input())
    L = [0] * (N + 1)
    R = [0] * (N + 1)
    P = [0] * (N + 1)

    for i in range(N):
        ND = list(input().split())
        P[int(ND[0])] = ND[1]
        if len(ND) >= 3 : L[int(ND[0])] = int(ND[2])
        if len(ND) >= 4 : R[int(ND[0])] = int(ND[3])
    word = ''
    subtree(1)
    print(f'#{T+1}',word)
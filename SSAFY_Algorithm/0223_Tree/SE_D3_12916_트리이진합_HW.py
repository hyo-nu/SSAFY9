# import sys;
#
# sys.stdin = open('input.txt')
#
#
# def enq(n):
#     global last
#     last += 1  # 완전이진트리에 마지막 정점을 추가하고
#     heap[last] = n  # 마지막 정점에 저장
#     c = last  # 부모가 있고, 부모 > 자식보다 큰지 검토
#     p = c // 2
#     while p > 0 and heap[p] < heap[c]:
#         heap[p], heap[c] = heap[c], heap[p]
#         c = p  # 옮긴 자리에서 부모와 비교하기 위해
#         p = c // 2
#     return
#
#
# Test = int(input())
#
# for T in range(Test):
#     N = int(input())
#     node = list(map(int, input().split()))
#
#     heap = [0] * (N + 1)
#     last = 0
#
#     for i in node:
#         enq(i)
#
#     print(heap[N])

import sys ; sys.stdin = open('input.txt')

def postorder(v):
    if v > N:
        return
    postorder(v * 2)
    postorder(v * 2 + 1)
    if N == v * 2:
        tree[v] = tree[v*2] + tree[v*2+1]

Test = int(input())

for T in range(Test):
    N,M,L = map(int,input().split())
    tree = [0] * (N + 1)

    for _ in range(M):
        l,N = map(int,input().split())
        tree[l] = N

    postorder(1)
    print(tree)







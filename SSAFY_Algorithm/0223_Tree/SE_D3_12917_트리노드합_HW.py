import sys
sys.stdin = open('input.txt')

def inorder(V):
    if V > N // 2:
        return
    inorder(V * 2)
    inorder(V * 2 + 1)
    if N == V * 2:
        G[V] = G[V * 2]
    else:
        G[V] = G[V * 2] + G[V * 2 + 1]


Test = int(input())

for T in range(Test):
    # N : 노드갯수, M : 리프노드수 , L : 출력할 노드번호
    N, M, L = map(int, input().split())
    G = [0] * (N + 1)

    for i in range(M):
        u, v = list(map(int, input().split()))
        G[u] = v

    inorder(1)
    print(f'#{T+1}',G[L])


#동훈스
#===============================================
def postorder(v):
    if v > N:
        return 0
    l = postorder(2 * v)
    r = postorder(2 * v + 1)
    T[v] += l + r
    return T[v]


T = int(input())
for tc in range(1, T + 1):
    N, M, L = map(int, input().split())
    T = [0] * (N + 1)
    for i in range(M):
        L_num, num = map(int, input().split())
        T[L_num] = num
    result = postorder(1)
    print(f'#{tc} {T[L]}')
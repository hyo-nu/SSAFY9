import sys;sys.stdin=open('input.txt')

def find_set(u):
    while u != rep[u]:
        u = rep[u]
    return u

def union_set(u,v):
    rep[find_set(v)] = find_set(u)

Test = int(input())

for TC in range(Test):
    V, E = map(int,input().split())
    rep = [i for i in range(V + 1)]
    G = []

    for _ in range(E):
        u, v, weight = map(int,input().split())
        G.append([u,v,weight])

    G.sort(key = lambda x:x[2])
    N = V + 1
    s = cnt = 0

    for u, v , weight in G:
        if find_set(u) != find_set(v):
            cnt += 1
            s += weight
            union_set(u,v)
            if cnt == N - 1:
                break

    print(f'#{TC+1}',s)





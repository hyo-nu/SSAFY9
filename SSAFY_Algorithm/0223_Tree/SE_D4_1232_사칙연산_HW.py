import sys ; sys.stdin = open('input.txt')

def calc(v):
    if len(c[v]) == 2:
        return int(c[v][1])

    l = calc(int(T[v][2]))
    r = calc()

for T in range(1):
    N = int(input())
    c = [[]]
    for i in range(N):
        c.append(list(input().split()))

    for i in c:
        print(i)
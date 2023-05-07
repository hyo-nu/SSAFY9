paper = int(input())

G = [[0]* 100 for _ in range(100)]
for i in range(paper):
    X,Y = map(int,input().split())
    for r in range(10):
        for c in range(10):
            G[X+r][Y+c] = 1

Sum = 0
for lst in G:
    Sum += sum(lst)
print(Sum)

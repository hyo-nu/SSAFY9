import sys;sys.stdin=open('input.txt')

Str1, Str2  = input(),input()
S1 , S2 = len(Str1), len(Str2)
G = [[0] * (S2+1) for i in range(S1+1)]

for i in range(S1):
    for j in range(S2):
        if Str1[i] == Str2[j]:
            G[i+1][j+1] = G[i][j] + 1
        else:
            G[i+1][j+1] = max(G[i][j+1],G[i+1][j])
print("[0, A, C, A, Y, K, P]")
for lst in G:
    print(lst)
print(G[-1][-1])

import sys
input = sys.stdin.readline

N = int(input())
S = []
for _ in range(N):
    x = list((input().split()))
    if x[0] == 'add':
         if int(x[1]) not in S : S.append(int(x[1]))
    elif x[0] == 'remove':
         if int(x[1]) in S : S.remove(int(x[1]))
    elif x[0] == 'check':
        if int(x[1]) in S : print(1)
        else : print(0)
    elif x[0] == 'toggle':
        if int(x[1]) in S : S.remove(int(x[1]))
        else : S.append(int(x[1]))
    elif x[0] == 'all':
         S = [i for i in range(1,21)]
    elif x[0] == 'empty':
         S =[]
S = input()
lst = sorted([S[i:len(S)] for i in range(len(S))])
for i in lst : print(i)

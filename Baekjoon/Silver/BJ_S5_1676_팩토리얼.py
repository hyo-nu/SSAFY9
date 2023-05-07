import sys;sys.stdin=open('input.txt')

N = int(input())
mul = cnt = 1
for i in range(1,N+1) : mul *= i
lst = list(str(mul))
for i in range(len(lst)-1,-1,-1):
    if lst[i] == '0': cnt += 1
    else : break
print(cnt-1)
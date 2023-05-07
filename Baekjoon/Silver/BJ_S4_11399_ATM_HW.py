import sys;sys.stdin=open('input.txt')
N = int(input())
time = sorted(list(map(int,input().split())))

Sum = total = 0
for T in time:
    Sum += T
    total += Sum
print(total)

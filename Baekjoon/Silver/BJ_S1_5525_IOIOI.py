import sys;sys.stdin=open('input.txt')

N = int(input())
M = int(input())
S = input().strip('O')
check = 'IOI'
i = cnt = pattern = 0
while i < len(S)-1:
    if S[i : i+3] == check:
        pattern += 1
        i += 2
    else:
        if pattern >= (N-1):
            cnt += pattern - (N-1)
        pattern = 0
        i += 1
print(cnt)

import sys ; sys.stdin = open('input.txt')
#  학생 수, 최대인원수
N, K = map(int,input().split())

room = [[0,0] for _ in range(6)]
for _ in range(N):
    S,Y = map(int,input().split())
    room[Y-1][S] += 1

cnt = 0
for lst in room:
    for i in lst:
        if i > 0 :
            if not i % K : cnt += i // K
            else : cnt += i//K + 1
print(cnt)
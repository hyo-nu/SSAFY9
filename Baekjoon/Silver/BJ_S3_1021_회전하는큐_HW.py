# 1. 왼쪽 pop
# 2. 왼쪽꺼 순환
# 3. 오른쪽꺼 순환

# 큐에 처음에 포함되어있던 수 N
# 지민이가 뽑아내려하는 원소 위치

# N : Q의크기 , M : 뽑아내려고하는 수의 개수
# N은 50보다 작은 M은 N보다 작은 수

from collections import deque
import sys ; sys.stdin = open('input.txt')

N, M = map(int,input().split())
nums = list(map(int,input().split()))

Q = deque()
for i in range(N):
    Q.append(i+1)

cnt = 0
while nums:
    p = nums.pop(0)
    posi = 0
    for i in range(len(Q)):
        if p == Q[i]:
            break
        posi += 1

    while p != Q[0]:
        # 왼쪽꺼 순환
        if posi <= len(Q)/2:
            out = Q.popleft()
            Q.append(out)
            cnt += 1
        # 오른쪽꺼 순환
        else:
            out = Q.pop()
            Q.appendleft(out)
            cnt += 1

    Q.popleft()

print(cnt)
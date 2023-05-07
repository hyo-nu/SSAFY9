import sys ; sys.stdin = open('input.txt')
from collections import deque
import sys
input = sys.stdin.readline

def DFS(n,lst):
    if n == M:
        # if lst not in Q:
        Q.append(lst)
        return
    x = 0
    for i in range(N):
        if not visited[i] and x != nums[i]:
            visited[i] = 1
            DFS(n + 1, lst + [nums[i]])
            visited[i] = 0
            x = nums[i]

N, M = map(int,input().split())
nums = list(map(int,input().split()))
nums.sort()
nums.append(0)
Q = deque()
visited = [0]*N
DFS(0,[])

for lst in Q:
    print(*lst)
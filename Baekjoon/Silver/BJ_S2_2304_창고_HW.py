import sys ; sys.stdin = open('input.txt')

pillar = int(input())
G = sorted([list(map(int,input().split())) for _ in range(pillar)],key = lambda x:x[0])

Max = 0
# 가장 큰 기둥 찾기
for i in range(pillar):
    print(G[i])
    if Max < G[i][1]:
        Max = G[i][1]
        high_idx = i

area = Max
print(area)
# 왼쪽 지붕
left = G[0][1] # 첫기둥 높이:
for i in range(high_idx): # 0,1,2
    area += (G[i+1][0] - G[i][0]) * left # (다음위치 - 현재위치) * 현재기둥높이
    print(f'left',area)
    if left < G[i+1][1]: # 기둥높이 변경여부 결정
        left = G[i+1][1]

# 오른쪽 지붕붕
right = G[pillar-1][1]
for i in range(pillar-1,high_idx,-1):
    area += (G[i][0] - G[i-1][0]) * right
    print(f'right', area)
    if right < G[i-1][1]:
        right = G[i-1][1]

print(area)


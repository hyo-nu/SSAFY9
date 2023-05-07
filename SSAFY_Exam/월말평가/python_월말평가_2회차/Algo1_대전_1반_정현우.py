Test = int(input())

# 가장 왼쪽 세로 줄부터 한 줄씩 띄어 나무를 심는다.

for T in range(Test):
    # N : 행 , M : 열
    # 3 <= N,M <= 20
    N, M = map(int,input().split())
    Tree = [list(map(int,input().split())) for _ in range(N)]
    price = 0   # 나무를 심는 총 비용
    cnt = 0      # 심은 나무의 총 갯수
    Max_p = 0     # 가장 비싼 나무

    for c in range(M):
        for r in range(N):
            if c % 2 == 0:
                price += Tree[r][c]       # 나무 비용의 합
                cnt += 1                  # 나무 갯수 세기
                if Max_p <= Tree[r][c]:   # 제일 비싼 나무
                    Max_p = Tree[r][c]    # 비싼 나무 업데이트
                    idx = c + 1           # 그 나무가 있는열

    print(f'#{T+1}',price,cnt,Max_p,idx)
# 나무 총 비용, 나무수, 비싼나무가격, 그 나무의 열 위치
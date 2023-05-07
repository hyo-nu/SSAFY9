# 오셀로
def change(R,C,BW):
    # 가로 변화

    # 세로 변화
    # 대각선 변화


Test = int(input())

# N : 보드 한변의 길이(4,6,8)중하나 , M : 돌을 놓는 횟수
for i in range(Test):
    N,M = map(int,input().split())

    # 오셀로 판 초기상태 일반화
    arr = [[0]*N for _ in range(N)]
    arr[N/2-1][N/2-1] = arr[N/2][N/2] = 2
    arr[N/2-1][N/2] = arr[N/2][N/2-1] = 1

    for j in range(M):
        C,R,BW = map(int,input().split())
        arr[R][C] = BW

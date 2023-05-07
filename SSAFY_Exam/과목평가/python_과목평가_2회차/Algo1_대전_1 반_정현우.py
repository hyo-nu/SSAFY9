Test = int(input())

for T in range(Test):

    N,M = map(int,input().split())         # N : 도화지의 크기 , M : 도장갯수
    arr = [[0]*N for _ in range(N)]        # 도화지 만들기
    cnt = 0
    for i in range(M): #
        R,C,W,H = map(int,input().split()) # 도장의 첫 위치와, 크기

        for h in range(H):                 # 도장 높이
            for w in range(W):             # 도장 너비
                arr[R+h][C+w] += 1         # (R,C) 위치부터 배열의 값을 1로 변경
                if arr[R+h][C+w] == 1:     # 1일 때만 cnt+=1
                    cnt +=1                # 1만 카운트 해야 겹치는 부분을 체크하지 않는다.

    print(f'#{T+1}' , cnt)
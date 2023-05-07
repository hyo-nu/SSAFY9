def photo(A,B,K,star):
    zoom = 0                              # 줌의 횟수
    while True:
        check = 0                         # 사진영역 안에 별 갯수를 확인
        AS,AE = valid_size(A,K)           # A,B 포인트 줌 영역이 범위를 벗어 나는가
        BS,BE = valid_size(B,K)

        # 사진 영역안에 별 갯수 확인
        for r in range(AS, AE):           # 사진영역 세로줄
            for c in range(BS, BE):       # 사진영역 가로줄
                if Map[r][c] == '*':
                    check += 1            # 별 갯수 check

        # 줌 할지 말지 결정 및 출력
        if zoom == 0 and check != star :  # 줌 아직 안했는데 별 갯수가, 다르면
            return -1                     # -1
        elif zoom >=0 and check == star:  # 줌을 했는데   별 갯수 같으면
                K -= 2                    # 줌 한번 더 해보기
                zoom += 1
        elif zoom >=0 and check != star:  # 별 갯수 다르면
                return zoom - 1           # 줌 갯수에 -1 리턴

# 사진영역이 지도영역의 범위를 벗어 나는지 확인
def valid_size(point,K):
    size = K // 2                         # 사진 영역의 절반
    start = point - size                  # size로 point 기준 시작점 설정
    end = point + size + 1                # size로 point 기준 끝점 설정
    if start < 0: start = 0               # start가 0보다 작으면 0
    if end > N: end = N                   # end가 N보다 크면 N
    return start,end

Test = int(input())

for T in range(Test):
    # 1 <= K(홀수) <= N <= 20
    # 0 <= A,B <= N
    N, K, A, B = map(int,input().split())
    star = 0                                # 별의 갯수
    Map = []                                # 하늘
    for r in range(N):
        s = list(input().split())           # 별 지도를 만들면서
        Map.append(s)
        for c in range(N):
            if s[c] == '*' : star += 1      # 별의 갯수를 확인

    print(f'#{T+1}',photo(A,B,K,star))
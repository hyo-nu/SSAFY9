Test = int(input())

for T in range(Test):
    N = int(input())                     # 두더지 N마리
    r,c = map(int,input().split())       # (r,c) 망치 위치
    catch = 0
    for i in range(N):                   # 두더지 마리수 만큼 반복
        A,B,K = map(int,input().split()) # (A,B) K 두더지 위치, K초 동안 나옴
        k = 1                            # 시작을 1초로 설정
        while k <= K:                    # K초 동안만 두더지가 나와있다.
            if B != c:                   # 좌우 이동이 우선순위를 가진다
                if B < c : c -= 1        # 두더지가 망치보다 좌측이면 좌로이동
                elif B > c : c += 1      # 두더지가 망치보다 우측이면 우로이동
                k += 1                   # 1회 움직임에 1초
            elif A != r:                 # 상하 이동은 좌우가 없을 때만 그래서 elif
                if A < r : r -= 1        # 두더지가 망치보다 위측이면 위로이동
                elif A > r : r += 1      # 두더지가 망치보다 아래측이면 아래로이동
                k += 1                   # 1회 움직임에 1초
        if r == A and c == B:            # K초 지나고 나와서 망치, 두더지 위치 같으면
            catch += 1                   # 두더지 잡았다.
    print(f'#{T+1}',catch)

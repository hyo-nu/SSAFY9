# 정사각형방

import sys;sys.stdin = open('input.txt')


# 1 <= Aij <= N**2이하
# 이동하려는 방이 현재 방 번호보다 1 커야함
# 어떤 방에서 시작해야 가장 많은 방을 이동하는지

# 상하좌우중 이동할 수 있는 곳 확인
def direction(mr, mc, nr, nc):
    if 0 <= mr < N and 0 <= mc < N and A[nr][nc] + 1 == A[mr][mc]:
        return True
    return False


def BFS(nr, nc, cnt):
    sr,sc = nr,nc               # nr,nc는 계속 업데이트, So 초기 시작점 저장
    info = Q.pop()              # 최대 방갯수를 가진 지점의 좌표와 방 갯수 가져오기
    while True:
        # 방 갯수 이동하며 세기
        if direction(nr, nc + 1, nr, nc): nc += 1 ; cnt += 1  # 우
        elif direction(nr + 1, nc, nr, nc): nr += 1 ; cnt += 1  # 하
        elif direction(nr, nc - 1, nr, nc): nc -= 1 ; cnt += 1  # 좌
        elif direction(nr - 1, nc, nr, nc): nr -= 1 ; cnt += 1  # 상
        else: # 이동 못하면 멈춰야지
            if info[2] < cnt:                                          # 방 갯수가 크면 새로운 데이터 없데이트
                Q.append([sr,sc,cnt]) ; return
            elif info[2] == cnt and A[info[0]][info[1]] >= A[sr][sc] : # 같으면 번호가 작은 방 확인
                Q.append([sr, sc, cnt]) ; return
            else :                                                     # 둘 다 아니면 다시 담아두기
                Q.append(info); return


Test = int(input())

for T in range(Test):
    N = int(input())
    A = [list(map(int, input().split())) for _ in range(N)]
    Q = [[0,0,0]]  # 초기위치, Max값 삽입

    for r in range(N):
        for c in range(N):
            BFS(r,c,1) # 각 좌표, 카운트 = 1로 삽입
    result = Q.pop() # 모든 확인이 끝나고 결과를 저장

    print(f'#{T+1}',A[result[0]][result[1]],result[2])


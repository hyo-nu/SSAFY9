# 오목
# 1 = 검은돌
# 2 = 흰돌
# 0 = 빈자리
# import sys;sys.stdin = open('input.txt')
#
# def Win():
#     dr = [0, 1, 1, 1, 0]  # 우대하대좌
#     dc = [1, 1, 0,-1,-1]
#
#     for r in range(N):
#         for c in range(N):
#             if con[r][c] != 0:
#                 for d in range(5):
#                     for i in range(1,5):
#                         nr = r + dr[d] * i
#                         nc = c + dc[d] * i
#                         if 0 <= nr <N and 0 <= nc < N:
#                             if con[nr][nc] == con[r][c]:pass
#                             else:break
#                         else : break
#                     else :
#                         nr += dr[d]
#                         nc += dc[d]
#                         if 0 <= nr <N and 0 <= nc < N:
#                             if con[nr][nc] != con[r][c] : return [con[r][c],r+1,c+1]
#                             else : return [0]
#                         else : return [con[r][c],r+1,c+1]
#     return [0]
#
# N = 19
# con = [list(map(int,input().split())) for _ in range(N)]
#
# info = Win()
# if len(info) > 1:
#     print(info[0])
#     print(info[1],info[2])
# else : print(info[0])
#
#
# #============================
# # 오목
# # 1 = 검은돌
# # 2 = 흰돌
# # 0 = 빈자리
# import sys;sys.stdin = open('input.txt')
#
# def Win():
#     dr = [0, 1, 1, 1, 0]  # 우대하대좌
#     dc = [1, 1, 0,-1,-1]
#
#     for r in range(N):
#         for c in range(N):
#             if con[r][c] != 0:
#                 for d in range(5):
#                     if 0 <= r-dr[d] <N and 0 <= c-dc[d] < N \
#                             and con[r-dr[d]][c-dc[d]] == con[r][c]:
#                         pass
#                     else:
#                         for i in range(1,5):
#                             nr = r + dr[d] * i
#                             nc = c + dc[d] * i
#                             if 0 <= nr <N and 0 <= nc < N:
#                                 if con[nr][nc] == con[r][c]:pass
#                                 else : break
#                             else : break
#                         else :
#                             lr = nr + dr[d]
#                             lc = nc + dc[d]
#                             if 0 <= lr <N and 0 <= lc < N:
#                                 if con[lr][lc] != con[r][c] :
#                                     if d >= 3:return [con[nr][nc], nr + 1, nc + 1]
#                                     else:return [con[r][c], r + 1, c + 1]
#                                 else : break
#                             else :
#                                 if d >= 3:return [con[nr][nc], nr + 1, nc + 1]
#                                 else:return [con[r][c], r + 1, c + 1]
#     return [0]
# N = 19
# con = [list(map(int,input().split())) for _ in range(N)]
#
# info = Win()
# if len(info) > 1:
#     print(info[0])
#     print(info[1],info[2])
# else : print(0)


#=========================================
import sys;sys.stdin = open('input.txt')

def Win():
    dr = [0, 1, 1, 1]  # 우대하대
    dc = [1, 1, 0,-1]

    for r in range(N):
        for c in range(N):
            if con[r][c] != 0:
                for d in range(4):
                    if 0 <= r-dr[d] <N and 0 <= c-dc[d] < N \
                            and con[r-dr[d]][c-dc[d]] == con[r][c]:
                        pass
                    else:
                        for i in range(1,5):
                            nr = r + dr[d] * i
                            nc = c + dc[d] * i
                            if 0 <= nr <N and 0 <= nc < N:
                                if con[nr][nc] == con[r][c]:pass
                                else : break
                            else : break
                        else :
                            lr = nr + dr[d]
                            lc = nc + dc[d]
                            if 0 <= lr <N and 0 <= lc < N:
                                if con[lr][lc] != con[r][c] :
                                    if d == 3:return [con[nr][nc], nr + 1, nc + 1]
                                    else:return [con[r][c], r + 1, c + 1]
                            else :
                                if d == 3:return [con[nr][nc], nr + 1, nc + 1]
                                else:return [con[r][c], r + 1, c + 1]
    return [0]
N = 19
con = [list(map(int,input().split())) for _ in range(N)]

info = Win()
if len(info) > 1:
    print(info[0])
    print(info[1],info[2])
else : print(0)
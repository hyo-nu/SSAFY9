def DFS(r,c):
    global Max
    dr = [-2, -1, 1, 2]
    dc = [1, 2, 2, 1]
    for d in range(4):
        nr = r + dr[d]
        nc = c + dc[d]
        if nr < 0 or nr >= N or nc < 0 or nc >= M:
            if sum(move) > 4:
                if 0 not in move:
                    Max = max(Max, sum([sum(lst) for lst in vi]))
                    return
                else: return
            else:
                Max = max(Max,sum([sum(lst) for lst in vi]))
                return
        else:
            if not vi[nr][nc]:
                vi[nr][nc] = 1
                move[d] += 1
                DFS(nr,nc)
                move[d] -= 1
                vi[nr][nc] = 0

N, M =map(int,input().split())
vi = [[0]*M for _ in range(N)]
move = [0] * 4
Max = 0
vi[N-1][0] = 1
DFS(N-1,0)
print(Max)

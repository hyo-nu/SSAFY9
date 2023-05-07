import sys ; sys.stdin = open('input.txt')

def road(lst):
    vi = [0] * N
    for i in range(N-1):
        if lst[i] == lst[i+1] : pass
        elif abs(lst[i]-lst[i+1]) == 1:
            if lst[i] < lst[i+1]:   # 오르막길
                for j in range(L):
                    if 0 <= i-j < N and lst[i] == lst[i-j] and vi[i-j] == 0 :
                        vi[i-j] = 1
                    else : return 0
            elif lst[i] > lst[i+1]: # 내리막길
                for j in range(L):
                    if 0 <= i+1+j < N and lst[i+1]== lst[i+1+j]:
                        vi[i+1+j] = 1
                    else : return 0
        else : return 0
    return 1

N,L = map(int,input().split())
G_row = [list(map(int,input().split())) for _ in range(N)]
G_col = list(map(list,zip(*G_row)))
road_cnt = 0

for i in range(N):
    a = road(G_row[i])
    b = road(G_col[i])
    road_cnt += a + b
print(road_cnt)
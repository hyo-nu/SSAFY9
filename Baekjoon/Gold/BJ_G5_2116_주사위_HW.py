import sys ; sys.stdin = open('input.txt')

def up_down(dice,up):
    for c in range(6):
        if dice[c] == up:
            if c == 0 : return dice[5]
            elif c == 1 : return dice[3]
            elif c == 2 : return dice[4]
            elif c == 3 : return dice[1]
            elif c == 4 : return dice[2]
            elif c == 5 : return dice[0]

N = int(input())
dice = [list(map(int,input().split()))for _ in range(N)]
# A B C D E F
# 0 1 2 3 4 5
# A-F : 0-5
# B-D : 1-3
# C-E : 2-4
Max = 0
for i in range(6):
    Sum = 0
    up = dice[0][i]
    down = up_down(dice[0],up)
    Sum +=max([c for c in dice[0] if c not in [up,down]])

    for j in range(1,N):
        up = down
        down = up_down(dice[j],up)
        Sum += max([c for c in dice[j] if c not in [up, down]])
    if Max < Sum:
        Max = Sum
print(Max)



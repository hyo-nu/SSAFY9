import sys ; sys.stdin = open('input.txt')
# 알파벳 : 열  A ~ H  => R
# 숫자   : 행  1 ~ 8  => C
def move(K_R, K_C, ST_R, ST_C,dr,dc):
    NK_R = K_R + dr
    NK_C = K_C + dc
    if 0 <= NK_R < 8 and 0 <= NK_C < 8:
        if NK_R == ST_R and NK_C == ST_C:
           if  0 <= ST_R+dr < 8 and 0 <= ST_C+dc < 8:
              return NK_R,NK_C,ST_R+dr,ST_C+dc
           else: return K_R, K_C, ST_R, ST_C
        else : return NK_R,NK_C,ST_R, ST_C
    else : return K_R, K_C, ST_R, ST_C

def find_value(R):
    for key, value in row.items():
        if value == R:
            return key

# L,LT,T,RT,R,RB,B,LB
D = {'L':0,'LT':1,'T':2,'RT':3,'R':4,'RB':5,'B':6,'LB':7}
row = {'A':0,'B':1,'C':2,'D':3,'E':4,'F':5,'G':6,'H':7}
dr = [-1,-1, 0, 1, 1, 1, 0,-1] # 위,대,우,대,아,대,왼,대
dc = [ 0, 1, 1, 1, 0,-1,-1,-1]

K,ST,N = input().split()
K_R,K_C = row.get(K[0]),int(int(K[1])-1)
ST_R,ST_C = row.get(ST[0]),int(int(ST[1])-1)

for _ in range(int(N)):
    po = input()
    d = D.get(po)
    K_R, K_C, ST_R, ST_C = move(K_R, K_C, ST_R, ST_C, dr[d], dc[d])

K_po = find_value(K_R) + str(K_C + 1)
ST_po = find_value(ST_R) +str(ST_C + 1)
print(K_po)
print(ST_po)

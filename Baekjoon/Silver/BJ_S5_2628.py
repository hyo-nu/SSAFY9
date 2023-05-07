c,r = map(int,input().split()) # 가로, 세로
cuts = int(input()) # 몇번잘라?

c_lst = [0,r]
r_lst = [0,c]
for i in range(cuts):
    line = list(map(int,input().split())) # 0:가로, 1:세로 , 점선번호
    if line[0] == 0 : c_lst.append(line[1])# 0가로
    elif line[0] == 1 : r_lst.append(line[1])# 1세로

c_lst.sort()
r_lst.sort()

max = 0
for i in range(len(c_lst)-1):# 0 1 2
    for j in range(len(r_lst)-1):# 0 1
        if max < (c_lst[i+1]-c_lst[i])*(r_lst[j+1]-r_lst[j]):
            max = (c_lst[i+1]-c_lst[i])*(r_lst[j+1]-r_lst[j])

print(max)
list
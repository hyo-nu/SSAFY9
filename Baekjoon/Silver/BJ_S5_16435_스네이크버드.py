L, H = map(int,input().split())
L_lst = sorted(list(map(int,input().split())))

num = 0
while num < L and L_lst[num] <= H:
    H ,num = H + 1, num + 1
print(H)



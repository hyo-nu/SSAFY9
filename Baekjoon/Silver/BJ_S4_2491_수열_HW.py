N = int(input())
num = list(map(int,input().split()))
result = []

cnt = 1
tmp = 0
mode = 0
for i in range(N-1):
    if mode == 0 :
        if num[i] == num[i + 1]: cnt += 1 ; tmp += 1
        elif num[i] < num[i + 1]: mode = 1 ; cnt += 1 ; tmp = 0
        elif num[i] > num[i + 1]: mode =-1 ; cnt += 1 ; tmp = 0
    else:
        if num[i] == num[i + 1] : cnt += 1 ; tmp += 1
        elif mode == 1 and num[i] < num[i + 1] : cnt += 1 ; tmp = 0
        elif mode == -1 and num[i] > num [i + 1] : cnt += 1 ; tmp = 0
        else :
            result.append(cnt)
            mode = mode * (-1)
            cnt = 2 + tmp
            tmp = 0
result.append(cnt)
if N == 1 :
    result.append(cnt);
result.sort()
print(result[-1])


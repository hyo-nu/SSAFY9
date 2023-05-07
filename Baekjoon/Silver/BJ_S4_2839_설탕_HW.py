N = int(input())

five = -1
ans = []
while five <= N:
    five += 1
    sugar = 0
    three = -1
    while sugar < N:
        three += 1
        sugar = (five * 5) + (three * 3)
        if sugar == N:
            ans.append([three+five,sugar])

if ans:print(ans[-1][0])
else : print(-1)

#=======================

n = int(input())
cnt_5 = n // 5
cnt_3 = (n - (cnt_5 * 5)) // 3

for i in range(cnt_5, -1, -1):
    cnt_3 = (n - i * 5) // 3
    if (i * 5) + (cnt_3 * 3) == n:
        print(i + cnt_3)
        break
else:
    print(-1)
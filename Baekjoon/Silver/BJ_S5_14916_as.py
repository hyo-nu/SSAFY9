money = int(input())
cnt_5 = money // 5
cnt_2 = (money -(cnt_5 * 5)) // 2

for i in range(cnt_5,-1,-1):
    cnt_2 = (money - i * 5) // 2
    if (i * 5) + (cnt_2 * 2) == money:
        print(i+cnt_2)
        break
else:
    print(-1)



Test = int(input())

for T in range(Test):
    word = input()

    for i in range(1, 6):
        for j in range(1, len(word) * 4 + 2):
            # 1,5번줄
            if i == 1 or i == 5:
                if (j + 1) % 4 == 0:
                    print('#', end='')  # 4n-1점화식, 3,7,11
                else:
                    print('.', end='')  # 나머지 .
            # 2,4번줄
            elif i % 2 == 0:
                if j % 2 == 0:
                    print('#', end='')  # 짝수면 #
                else:
                    print('.', end='')  # 홀수면 .
            # 3번줄
            elif i == 3:
                if (j + 1) % 4 == 0:
                    print(word[((j + 1) // 4) - 1], end='')  # 4n-1점화식, 3,7,11
                elif j % 2 == 0:
                    print('.', end='')  # 짝수면 .
                else:
                    print('#', end='')  # 나머지 #

        print()



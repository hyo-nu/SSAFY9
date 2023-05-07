# 둘
Test = int(input())
# Test = 10

for T in range(Test):

    # N, M = map(int,input().split())
    word = input()
    N = len(word)
    check = 0
    for i in range(N//2):
        if word[i] != word[N-i-1]:
            break
    else:
        check += 1
    if check == 1 : print(f'#{T + 1}', 1)
    else : print(f'#{T + 1}', 0)

# 처음
Test = int(input())

for T in range(Test):
    word = input()
    N = len(word)
    cnt = 0
    for i in range(N//2):
        if word[i] == word[N - i - 1]:
            cnt += 1
        elif word[i] != word[N - i - 1]:
            print(f'#{T+1}', 0)
            break
    if cnt == N//2:
        print(f'#{T + 1}', 1)
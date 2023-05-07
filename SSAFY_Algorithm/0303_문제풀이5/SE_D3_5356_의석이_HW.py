import sys ; sys.stdin = open('input.txt')

Test = int(input())

for T in range(Test):
    String = [[] for _ in range(15)]
    for r in range(5):
        word = list(input())
        for c in range(len(word)):
            String[c] += [word[c]]

    print(f'#{T+1}',end = ' ')
    for S in String:
        print(''.join(S), end = '')
    print()



import sys ; sys.stdin = open('input.txt')

Test = int(input())

    # N : 컨테이너 수 3
    # M : 트럭 수 2
for T in range(Test):
    N,M = map(int,input().split())
    weigh = sorted(list(map(int,input().split())),reverse = True)  # N개 화물 무게
    ton = sorted(list(map(int,input().split())),reverse = True)  # M개 트럭의 적재용량
    
    result = 0
    for w in range(N):
        for t in range(len(ton)):
            if weigh[w] <= ton[t]:
                result += weigh[w]
                ton.pop(0)
                break

    print(f'#{T+1}',result)
    print()

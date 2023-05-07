import sys ; sys.stdin = open('input.txt')

Test = int(input())

for TC in range(Test):
    N, M = map(int,input().split()) # 컨테이너, 트럭
    w_lst = sorted(list(map(int,input().split())),reverse=True)# 컨테이너별 무게
    t_lst = sorted(list(map(int,input().split())),reverse=True)# 트럭 적재용량
    total_w = w = t = 0
    print(w_lst)
    print(t_lst)
    while w < N and t < M:
        if w_lst[w] <= t_lst[t]:
            total_w += w_lst[w]
            t += 1
        w += 1

    print(f'#{TC+1}', total_w)
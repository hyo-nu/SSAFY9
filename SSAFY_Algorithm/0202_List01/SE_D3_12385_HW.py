# 두 번째풀이
Test = int(input())

for T in range(Test):
    K, N, M = map(int, input().split())
    charge_stop = list(map(int, input().split()))

    now_point = K  # 이동한 지점을 처음으로 생각하고 충전소확인
    charge = 0
    while now_point < N:  # 현지점이 도착지보다 작을때만
        for _ in range(K):
            if now_point in charge_stop:  # 현지점에 충전소 있는지
                charge += 1  # 있으면 충전하고 for문 탈출
                break
            else:
                now_point -= 1  # 없으면 현지점에서 한칸 빡구
        else:  # for문 3사이킁 다 돌았다는건 충전소가 없었다는 것
            print(f'#{T + 1}', 0)
            break
        now_point += K  # 현지점에서 3칸 더 이동해서 다시 반복

    if now_point >= N: print(f'#{T + 1}', charge)

# 첫번째 풀이
Test = int(input())

for T in range(Test):
    # K = 한번 충전으로의 최대 이동거리
    # N = 종점
    # M = M개의 충전기
    K, N, M = map(int, input().split())
    M_stop = list(map(int, input().split()))

    charge_stop = [0] * N
    for i in M_stop:
        charge_stop[i] += 1

    now_distance = 1
    charge_cnt = 0
    distance_change = 1

    while now_distance < N:
        # print(f'현위치:{now_distance}, 몇칸 전진:{distance_change}')
        if distance_change == K:  # 3칸을 전진했다
            distance_change = 0
            if charge_stop[now_distance] == 1:  # 3칸 전진 했을 때 현 지점에 충전기 있으면
                charge_cnt += 1  # 한번 충전
            elif charge_stop[now_distance] == 0:  # 3칸 전진했을 때 현 지점에 충전기 없으면
                stop_cnt = 0
                for i in range(1, K):  # 이전에 충전기 있었는지 확인
                    if charge_stop[now_distance - i] == 1:  # 이전에 있었으면
                        charge_cnt += 1  # 충전 한번 하고
                        now_distance -= i  # 뒤로간 곳을 현위치로 설정
                        break  # for문 그만
                    elif charge_stop[now_distance - 1] == 0:  # 이전에 없으면
                        stop_cnt += 1  # 버스를 터트릴 준비를 한다.
                if stop_cnt == K - 1:  # 3칸 전진 전 지점에 도달 지전까지 충전소 없으면
                    print(f'#{T + 1} 0')  # 버스 폭발
                    break

        now_distance += 1
        distance_change += 1
    if stop_cnt != K - 1:
        print(f'#{T + 1} {charge_cnt}')
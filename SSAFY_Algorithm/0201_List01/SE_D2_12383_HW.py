Test = int(input())

for T in range(Test):
    N = int(input())
    nums = list(map(int, input().split()))
    room = [0] * 100

    # 회전 했을때 쌓인 상자의 갯수 리스트
    for i in range(100):
        for j in range(N):
            if nums[j] >= i + 1: room[i] += 1

    # 낙차 계산
    fall_max = 0
    for i in range(len(room)):  # 상자가 쌓인 장소갯수
        for j in range(N):  # 회전 후 가장 위에 있는 상자의 이전 위치찾기
            if nums[j] >= i + 1:
                if fall_max < (N - room[i]) - j:  # (전체- 상자갯수) = 떨어진 수 있는 공간
                    fall_max = (N - room[i]) - j  # 상자의위치(i)를 빼면 낙차가 구해짐

    print(f'#{T + 1}', fall_max)
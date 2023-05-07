# 길찾기

# 현우스 코드
Test = 10

for T in range(Test):
    TC, E = map(int,input().split())

    G = [[] for _ in range(100)]            # 정점이 0~99 ,인접 제작을 위한 배열
    E_lst = list(map(int,input().split()))  # 간선을 일열로 쭉 입력

    for i in range(len(E_lst)-1):
        if i % 2 == 0 : G[E_lst[i]].append(E_lst[i+1]) # E_lst에서 홀 수 번쨰 요소를 G의 행으로
                                                       # 짝수번쨰 요소를 열로 넣는다
    S = []                  # Stack 만들고
    visited = [0] * 100     # 지나온 길 확인 list
    v = 0                   # 현재 정점
    S.append(v)             # while 시작을 위한 Stack추가
    visited[v] = 1          # 현재 정점을 들렸다
    land = 0                # 도착지 확인을위한 변수

    while S:
        for i in G[v]:      # 현재 정점에서 갈 수 있는 정점 리스트
            if not visited[i]: # 갈 수 있는 정점이 방문한 곳 아니라면
                S.append(v)    # 현재 정점 stack에 추가
                visited[i] = 1 # 다음 위치 들렸다고 표시하고
                v = i          # 현재 정점으로 변경
                if v == 99: land +=1 # 현재 정점 99면 도착했다고 표시
                break
        else: # 전부다 방문한 리스트인 경우
             v = S.pop() # 뒤로 돌아가기
    print(f'#{T + 1}', end=' ')
    if land != 0 : print(1)
    else : print(0)

## 동훈스 코드
def start2End(graph):
    S = []
    visited = [0] * 100
    v = 0
    S.append(0)

    while S:
        if visited[99] == 1:
            return 1

        for i in G[v]:
            if not visited[i]:
                S.append(v)
                visited[i] = 1
                v = i
                break
        else:
            v = S.pop()
    return 0


T = 10
for tc in range(1, T + 1):
    t, road = map(int, input().split())
    road_lst = list(map(int, input().split()))
    G = [[] * 100 for _ in range(100)]

    for i in range(road):
        v1, v2 = road_lst[i * 2], road_lst[i * 2 + 1]
        G[v1].append(v2)

    print(f'#{tc} {start2End(G)}')
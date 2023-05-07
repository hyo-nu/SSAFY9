# 피자굽기

# # 도미노피자
# def enQueue(item):
#     global rear
#     if front == (rear + 1) % size:
#         return
#     rear = (rear + 1) % size
#     Q[rear] = item
#
#
# def deQueue():
#     global front
#     if front == rear:
#         return
#     front = (front + 1) % size
#     return Q[front]
#
# Test = int(input())
#
# for TC in range(Test):
#     N, M = map(int, input().split())  # N 화덕의 크기, M 피자갯수
#     C = list(map(int, input().split()))  # 피자마다 치즈의양
#     c_lst = [[C[i], i + 1] for i in range(M)]  # 피자치즈양 , 피자번호
#
#     size = N + 1  # 화덕에 더미공간 추가
#     front = rear = 0
#     Q = [[] for _ in range(size)]  # 화덕 제작
#     for i in range(N): enQueue(c_lst[i])  # 화덕에 피자 넣기
#     remain = M - N  # 피자갯수 - 화덕수
#     cycle = 0
#     print(Q)
#
#     while front != rear:
#         out = deQueue()  # 화덕 한번 돌아감
#         enQueue(out)
#         cycle += 1
#         print(f'cycle:{cycle}, f :{front} r:{rear},{Q}')
#         # 한번 사이클 돌면 치즈가 녹음
#         if cycle % N == 0:
#             for i in range(size):
#                 if i != front:
#                     Q[i][0] = Q[i][0] // 2
#             print(f'녹았다:{Q}')
#
#         if Q[(front + 1) % size][0] == 0:
#             print(f'DeQ전 f :{front} r:{rear},{Q}')
#             result = deQueue()
#             print(result)
#             print(f'DeQ후 f :{front} r:{rear},{Q}')
#             remain += 1
#             if remain < M:
#                 enQueue(c_lst[remain])
#                 print(f'enQ후 f :{front} r:{rear},{Q}')
#
#     print(f'#{TC + 1}', end=' ')
#     print(result)

# 미스터 피자
def enQueue(item):
    global rear
    if front == (rear + 1) % size:
        return
    rear = (rear + 1) % size
    Q[rear] = item


def deQueue():
    global front
    if front == rear:
        return
    front = (front + 1) % size
    return Q[front]


Test = int(input())

for TC in range(Test):
    oven, pi_cnt = map(int, input().split())  # 화덕크기, 피자갯수
    pi = list(map(int, input().split()))  # 각 피자의 치즈양
    pi_num = [[pi[i], i + 1] for i in range(pi_cnt)]  # [치즈양 , 피자번호]

    size = oven + 1  # 화덕 사이즈 1 추가 , 원형큐를 위한 작업
    Q = [[] for _ in range(size)]
    front = rear = 0

    for i in range(oven):  # enQ
        enQueue(pi_num[i])

    remain = oven # 남아있는 피자
    while front != rear:
        pizza = deQueue()
        pizza[0] = pizza[0] // 2
        result = pizza[1]

        if pizza[0] == 0:
            if oven < pi_cnt:
                enQueue(pi_num[oven])
                oven += 1
        else :
            enQueue([pizza[0],pizza[1]])

    print(f'#{TC+1}', result)



















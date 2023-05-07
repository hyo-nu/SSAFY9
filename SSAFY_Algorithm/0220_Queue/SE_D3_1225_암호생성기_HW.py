# 원형
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


Test = 10

for TC in range(Test):
    T = int(input())
    Q = [0]
    Q.extend((list(map(int, input().split()))))
    N,size = 8,9
    front, rear = 0,8
    minus = 0

    while Q[rear] != 0:
        out = deQueue() - (minus % 5+1)
        minus += 1
        if out < 0 : out = 0
        enQueue(out)

    print(f'#{T}', end=' ')
    print(*Q[(front+1) % size : size],*Q[0:(front+1) % size -1])







#===============================================
# 선형
def enquenu(item):
    global rear
    rear += 1
    Q[rear] = item

def dequeue():
    global front
    front += 1
    return Q[front]




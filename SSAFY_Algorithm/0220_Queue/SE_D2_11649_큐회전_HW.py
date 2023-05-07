
#=======================================================
# 선형
def enqueue(item):
    global rear
    rear += 1
    rear = rear
    Q[rear] = item

def dequeue():
    global front
    front +=1
    return Q[front]

#=====================================================
# 원형 큐

def isEmpty():
    return front == rear

def peek():
    return Q[front+1]

def enQueue(item):
     global rear
     if front == (rear + 1) % (N+1):
        return
     rear = (rear + 1) % (N+1)
     Q[rear] = item

def deQueue():
    global front
    if front == rear:
        return
    front = (front + 1) % (N+1)
    return Q[front]

#==========================================

Test = int(input())

for TC in range(Test):
    N, M = map(int, input().split())
    nums = list(map(int, input().split()))

    Q = [0] * (N + 1)
    front = rear = 0
    for i in range(0, N):
        enQueue(nums[i])
        print(f'front : {front},rear : {rear}')
        print(Q)
    print()
    for i in range(M):
        out = deQueue()
        enQueue(out)
        print(f'front : {front},rear : {rear}')
        print(Q)
    print(f'#{TC + 1}', end=' ')
    print(Q[(front + 1) % (N + 1)])
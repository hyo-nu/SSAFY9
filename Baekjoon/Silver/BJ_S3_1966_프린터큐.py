import sys;sys.stdin=open('input.txt')
from collections import deque

Test = int(input())
for TC in range(Test):
    N, M = map(int,input().split())
    order = list(map(int,input().split()))
    order_lst = deque(enumerate(order))
    order_max = deque(sorted(order,reverse=True))
s
    turn = 0
    target = [100,10]
    while target[0] != M:
        if order_lst[0][1] == order_max[0]:
            target = order_lst.popleft()
            order_max.popleft()
            turn += 1
        else :
            order_lst.rotate(-1)
    print(turn)
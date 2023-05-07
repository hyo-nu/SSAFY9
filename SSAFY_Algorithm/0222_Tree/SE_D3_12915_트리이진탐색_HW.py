# def inorder(v):
#     global value
#     if v > N:
#         return
#
#     inorder(v * 2)
#     value += 1
#     node[v] = value
#     inorder(v * 2 + 1)
#
#
# Test = int(input())
#
# for T in range(Test):
#     N = int(input())        # N 까지의 자연수
#     node = [0] * (N + 1)    # 인덱스 매칭하기 위해 공간 추가
#     value = 0
#     inorder(1)
#     print(f'#{T + 1}', node[1], node[N // 2])
import sys;sys.stdin = open('input.txt')

def inorder(v):
    global value
    if v > N:
        return

    inorder(v * 2)
    value += 1
    node[v] = value
    inorder(v * 2 + 1)

Test = int(input())

for T in range(Test):
    N = int(input())
    node = [0] * (N + 1)
    value = 0
    inorder(1)

    print(f'#{T+1}', node[1],node[N//2])
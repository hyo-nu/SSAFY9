def perm(k):

    global Min
    if k == N-2:

        # A보다 B가 먼저 나온 경우를 제외
        for i in range(N-1):
            if arr[i] == A:A_Idx = i
            if arr[i] == B:B_Idx = i
        if A_Idx > B_Idx : return
        lst = [0]+arr+[0]
        Sum = 0
        for i in range(len(lst)-1):
            Sum += G[lst[i]][lst[i+1]]
        if Min > Sum:
            Min = Sum
        return

    # 순열을 만들어준다.
    for i in range(k,N-1):
        arr[k],arr[i]=arr[i],arr[k]
        perm(k+1)
        arr[k],arr[i]=arr[i],arr[k]

Test = int(input())

for TC in range(Test):
    N = int(input())
    G = [list(map(int,input().split())) for _ in range(N)]
    A,B = map(int,input().split())
    arr = [i for i in range(1,N)]
    Min = 99999999
    perm(0)
    print(f'#{TC+1}',Min)
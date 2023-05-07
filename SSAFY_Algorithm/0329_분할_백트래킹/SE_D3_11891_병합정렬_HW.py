import sys;sys.stdin=open('input.txt')

def merge_sort(s,e):
    global cnt
    if s == e :
        return

    mid = (s + e) // 2 #   5//2 = 2
    if (s + e) % 2 == 0 : mid -= 1
    merge_sort(s,mid) # 0,1,
    merge_sort(mid+1,e) # 2,3,4

    i,j,k = s, mid+1, s
    # print(f'i:{i},j:{j},k:{k}')
    # print(f'left = {s} ~ {mid}')
    # print(f'right = {mid+1} ~ {e}')

    if arr[mid] > arr[e]:
        cnt += 1

    while i <= mid and j <= e:
        if arr[i] < arr[j]:
            tmp[k] = arr[i] ; i, k = i + 1, k + 1
        else:
            tmp[k] = arr[j] ; j, k = j + 1, k + 1

    while i <= mid:
        tmp[k] = arr[i] ; i, k = i + 1, k + 1
    while j <= e:
        tmp[k] = arr[j] ; j, k = j + 1, k + 1

    for i in range(s,e+1):
        arr[i] = tmp[i]

    # print(arr)
    # print()

Test = int(input())

for TC in range(Test):
    N = int(input())
    arr = list(map(int,input().split()))
    tmp = [0] * N
    cnt = 0
    merge_sort(0,N-1)
    print(f'#{TC+1}',arr[N//2], cnt)
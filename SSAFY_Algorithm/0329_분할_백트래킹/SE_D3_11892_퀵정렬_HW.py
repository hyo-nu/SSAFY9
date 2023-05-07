def quick_lomuto(ST,EP): # 0 , 4
    if ST >= EP:
        return
    i = ST - 1 # -1

    for j in range(ST,EP): # 0 , 4
        if lst[j] <= lst[EP]:
            i += 1
            lst[i], lst[j] = lst[j], lst[i]
    i += 1
    lst[i],lst[EP] = lst[EP], lst[i]
    quick_lomuto(ST,i-1)
    quick_lomuto(i+1,EP)

Test = int(input())

for TC in range(Test):
    N = int(input())
    lst = list(map(int,input().split()))
    quick_lomuto(0,len(lst)-1)
    print(f'#{TC+1}',lst[N//2])


def quick_hoare(lo,hi):
    if lo >= hi : return
    i , j = lo, hi
    p = lst[lo]

    while i <= j:
        while i <= hi and p >= lst[i]:
            i += 1
        while p < lst[j]:
            j -= 1
        if i < j:
            lst[i], lst[j] = lst[j], lst[i]

    lst[lo], lst[j] = lst[j], lst[lo]
    quick_hoare(lo, i-1)
    quick_hoare(i+1,hi)

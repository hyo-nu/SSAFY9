# 모음 1개 , 자음 2개
def back(n, lst):
    if n > C - 1:
        if len(lst) == L :
            cnt = 0
            for i in lst:
                if i in vowels:
                    cnt += 1
            if 1 <= cnt <= L-2 :
                ans.append(lst)
        return

    back(n+1, lst + [alpa[n]])
    back(n+1, lst)


vowels = ['a', 'e', 'i', 'o', 'u']
L, C = map(int, input().split())
alpa = sorted(list(input().split()))
ans = []
back(0, [])

for lst in ans:
    print(''.join(lst))
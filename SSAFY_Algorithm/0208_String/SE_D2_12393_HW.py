# 둘

Test = int(input())
# Test = 10

def bf_for(tot,pat):
    t = len(tot) # 10
    p = len(pat) # 4
    cnt = 0
    for i in range(t-p+1): # 0 1 2 3 4 5 6
        for j in range(p): # (6789)
            if tot[i+j] != pat[j]:
                break
        else:
            cnt += 1
    return cnt

for T in range(Test):

    # N, M = map(int,input().split())
    pat = input()
    tot = input()

    print(f'#{T + 1}',bf_for(tot,pat))

# 첫
Test = int(input())

for T in range(Test):
    str1 = input()
    N = len(str1)
    str2 = input()
    M = len(str2)

    cnt = 0
    for i in range(0,M-N+1): # M-N+1은 작은N이 M위를 따라 움직이는 거리
        if str2[i:i+N] == str1 : cnt += 1 # i번째에서 시작하여 N과 같은 크기 만큼 슬라이싱해서
                                          # str1과 값이 같으면 cnt 업
    if cnt >= 1 : print(f'#{T+1} 1') # cnt가 1이상이면 같은게 있다
    else : print((f'#{T+1} 0')) # cnt가 0이면 같은거 없다.
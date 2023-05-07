# 첫째 무조건 0
# 두번째 0,1
# 0은 제자리, 1은 바로 앞으로
# 세번째 0,1,2
# 뽑은 번호만큼 앞자리로
N = int(input())
num = list(map(int,input().split()))
lst = []
ST = 1

for i in num:
    if i == 0 : lst.append(ST)
    else : lst.insert(len(lst)-i,ST)
    ST += 1

print(*lst)
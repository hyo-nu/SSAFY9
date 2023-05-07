# 입력 예시
# [1, 1, 3, 3, 0, 1, 1]

# 출력 예시
# [1, 3, 0, 1]

num_lst = list(map(int,input('0~9까지의 정수 입력 : ').split()))
num_lst_new = []
num_lst_new.append(num_lst[0])

for n in range(0,len(num_lst)-1):
    if num_lst[n] != num_lst[n+1]:
        num_lst_new.append(num_lst[n+1])
print(num_lst_new)


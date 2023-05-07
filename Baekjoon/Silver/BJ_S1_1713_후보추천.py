# 1 <= N <= 20
# 1 <= 추천 <= 2000
# 1 <= 학생 <= 100

N = int(input())
sug = int(input())
stud = list(map(int,input().split()))
number = [0] * 101
photo = 0

for i in stud:
    number[i] += 1



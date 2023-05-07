
val = 'algorithm'

rev_str = ''
for i in range(len(val)-1,-1,-1):
	rev_str += val[i]
print(rev_str)

#=========================
# 교환을 위해 리스트로 한글자씩 저장
val = list(val)
N = len(val)
for i in range(N//2):
    val[i], val[N-1-i] = val[N-1-i], val[i]
print(val)


num = 4567
num_str = ''
while num:
    digit = num % 10
    num = num // 10
    num_str = chr(ord('0') + digit) + num_str

print(num_str,type(num_str))

#===================================
# 모든 패턴이 있을 수 있는 시작위치
n = len(t)
m = len(p)

for i in range(0,n-m+1):
    # found = True  # 플래그 변수
    for j in range(m):
        if p[j] != t[i+j]:
            break
    else:
        # 잡았다 요놈..

string = input()

count = 0
def leng (s):
    s_list = list(s)
    count = 0
    for c in s_list:
        count += 1
    return count

if leng(string) % 2 != 0: #홀수
    print(string[leng(string) // 2])

elif leng(string) % 2 == 0: #짝수
    print(string[leng(string) // 2-1],string[leng(string) // 2])



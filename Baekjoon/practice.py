<<<<<<< HEAD
def f(x):
    total = 1
    for i in x:
        total *= int(i)
    return total


num = input()
idx = 1
while True:
    if idx == len(num):
        idx = 'NO'
        break
    if f(num[:idx]) == f(num[idx:]):
        print(num[:idx],num[idx:])
        idx = 'YES'
        break
    idx += 1
print(idx)
=======
Str = input()
S = ''
for s in Str:
    if s.isalpha():
        if 65 <= ord(s) <= 90: # 대문자
            s = ord(s) + 13
            if s > 90:
                s -= 26
        else : # 소문자
            s = ord(s) + 13
            if s > 122:
                s -= 26
        s = chr(s)
    S+=s

print(S)
>>>>>>> 592bb0591a46cb5d717bde5046a40f38162b2b60

import sys;sys.stdin = open('input.txt')

S = input()
T = input()

result = 0
while len(S) <= len(T):
    if T[-1] == 'A':
        T = list(T)
        T.pop()
        T = ''.join(T)

    elif T[-1] == 'B':
        T = list(T)
        T.pop()
        T.reverse()
        T = ''.join(T)

    if S == T:
        result = 1

print(result)

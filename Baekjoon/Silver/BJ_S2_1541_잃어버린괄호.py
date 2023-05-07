import sys;sys.stdin=open('input.txt')

fx = input() + '+'
tmp = ''
minus = 0
sm = 0
for s in fx:
    if s.isdigit() : tmp += s
    else :
          if not minus : sm += int(tmp) ; tmp = ''
          elif minus : sm -= int(tmp) ; tmp = ''
          if s == '-': minus = 1

print(sm)
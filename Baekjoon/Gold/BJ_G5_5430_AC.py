import sys;sys.stdin=open('input.txt')
Test = int(input())

for TC in range(Test):
    RD = input()
    n = int(input())
    if n > 0 : n_lst = list(map(int,input().rstrip("]").lstrip("[").split(",")))
    else : n_lst = input()

    SP, EP = 0, n-1
    R_mode = 0
    for rd in RD:
        if SP > EP and rd == "D" : result = "error" ; break
        else:
            if rd == "R" and not R_mode: R_mode = 1
            elif rd == "R" and R_mode: R_mode = 0
            elif rd == "D" and not R_mode: SP +=1
            elif rd == "D" and R_mode: EP -=1
    else:
        if SP != EP + 1:
            n_lst = n_lst[SP:EP + 1]
            if R_mode : n_lst.reverse()
            result = "["
            for idx,n in enumerate(n_lst):
                result += str(n)
                if idx < len(n_lst)-1: result += ","
            result += "]"
        else : result = "[]"
    print(result)


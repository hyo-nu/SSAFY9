A,B = map(str,input().split())
N = len(A) # 9
M = len(B) # 8

i_same = -1
for i in range(M): # 0 1 2 3 4 5 6 7 8
    for j in range(N): # 0 1 2 3 4 5 6 7 
        if str(A[i]) == str(B[j]):
            i_same = i
            j_same = j
            break
    if i_same != -1:
        break    

for i in range(M): # 0 1 2 3 4 5 6
    for j in range(N): # 0 1 2 3 4 5
        if i == j_same : print(A,end = '') ; break
        elif j == i_same : print(B[i], end = '')
        else : print('.',end ='')
    print()
             
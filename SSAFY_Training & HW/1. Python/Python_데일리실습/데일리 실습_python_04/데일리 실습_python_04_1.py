error = 0

while True:
    passward = [3,2,7,9]
    passward_check = list(map(int,input().split()))
    
    if passward_check == passward:
        print('yes')
        break
    else:
        error += 1
        if error == 3:
            print('3회 이상 실패로 인해 입력불가함')
            break
            
import sys;sys.stdin = open('input.txt')

Test = int(input())

for TC in range(Test):
    two = list(input())
    three = list(input())
    lst = [i for i in range(3)] # 1,2,3
    stop = 0
    for i in range(len(two)):
        two[i] = str((int(two[i]) + 1) % 2)
        for j in range(len(three)):
            for k in range(1,3):
                three[j] = str((int(three[j]) + k) % 3)
                num1 = int(''.join(two),2)
                num2 = int(''.join(three),3)
                if num1 == num2 :
                    stop = 1 ;
                    break
                three[j] = str((int(three[j]) + (3-k)) % 3)
        two[i] = str((int(two[i]) + 1) % 2)
        if stop : break
    print(f'#{TC+1}', num1)





a,b = map(int,input().split())

lst = []
for i in range(1,46):
    for j in range(i):
        lst.append(i)

sum = 0
for j in range(a-1,b):
    sum += lst[j]
print(sum)





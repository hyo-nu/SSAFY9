
fruit_lst = input().lower().split(',')

for f in range(len(fruit_lst)):
    if  fruit_lst[f][:6] == 'rotten':
        fruit_lst[f] = fruit_lst[f][6:]
print(fruit_lst)


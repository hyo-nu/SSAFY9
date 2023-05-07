infos = [{'name': 'kim', 'age': 12}, {'name': 'lee', 'age': 4}]

sum = 0
for i in infos:
    sum += i.get('age')
print(sum)
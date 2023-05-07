sort_amount = []
sort_water = []

while True:
    sort = list(input('소금물 퍼센트 농도와 소금물의 양 : ').split())
    if len(sort) == 1:
        if sort[0] == 'Done':
            break 
    sort_amount.append(int(sort[0])*int(sort[1])/100)
    sort_water.append(int(sort[1]))

result_sort_percent = sum(sort_amount)/sum(sort_water)*100
result_sort_water = sum(sort_water)


print(round(result_sort_percent,2),round(result_sort_water,2))
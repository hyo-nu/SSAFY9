# 입력 예시
# # mass percent.py 실행 시
# 1.소금물의 농도(%)와 소금물의 양(g)을 입력하십시오: 1% 400g
# 2.소금물의 농도(%)와 소금물의 양(g)을 입력하십시오: 8% 300g
# Done

# 출력 예시
# 4.0% 700.0g

list_solt = []
list_amount = []

def mass_percent(per_amount):
    
    
    list_solt.append(int(per_amount[0].replace('%','')) * int(per_amount[1].replace('g',''))/100)
    list_amount.append(int(per_amount[1].replace('g','')))

    return list_solt, list_amount

for n in range(6):  
    per_amount = input(f'{n+1}.소금물의 농도(%)와 소금물의 양(g)을 입력하십시오: ').split()  
    
    if per_amount == ['done']:    
        break    
    list_solt, list_amount = mass_percent(per_amount)

result_per = sum(list_solt)/sum(list_amount)*100
result_amount = sum(list_amount)

lst = str(result_per).split('.')
if len(lst[1]) < 2:
    print(f'{result_per}% {result_amount:.1f}g')
else:
    print(f'{result_per:.2f}% {result_amount:.1f}g')

 

# 함수 없는 코드

# list_amount = []
# list_per = []
# for n in range(6):
#     per_amount = input(f'{ n +1}.소금물의 농도(%)와 소금물의 양(g)을 입력하십시오: ').split()
#     print(per_amount)
#     print(type(per_amount))
#     if per_amount == ['done']:
#         break
#     else:
#         list_amount.append(int(per_amount[0].replace('%', '')))
#         list_per.append(int(per_amount[1].replace('g', '')))
#         result_amount = sum(list_amount)
#         result_per = sum(list_per) / sum(list_amount) * 100

# print(f'{result_per:.2f}% {result_amount:.2f}g')

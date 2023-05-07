orders = '아이스아메리카노,카라멜마키야또,에스프레소,\
아메리카노,아메리카노,아이스라떼,핫초코,아이스아메리카노,\
아메리카노,아이스카라멜마키야또,아이스라떼,라떼마키야또,\
카푸치노,라떼마키야또'

list_orders = orders.split(',')

order_dict = {}

for order in list_orders:

    if order in order_dict:
        order_dict[order] = order_dict[order] + 1
    else:
        order_dict[order] = 1
        
print(order_dict)

# 위 코드 한줄로 줄이기
# order_dict[order] = order_dict.get(order, 0) + 1
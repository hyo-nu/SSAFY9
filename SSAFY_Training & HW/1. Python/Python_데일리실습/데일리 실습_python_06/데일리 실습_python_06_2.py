grain_lst = [('고구마',3000), ('감자',2000), ('옥수수',4500),('토란',1300)]

grain_max_cost = 0

for grain in grain_lst:
    if grain[1] >= grain_max_cost:
        grain_max_cost = grain[1]
        result = grain[0]
        
print(result)
    


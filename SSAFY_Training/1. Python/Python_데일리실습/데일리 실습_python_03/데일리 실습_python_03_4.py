blood_types = [ 'A','A','O', 'B', 'A', 'O', 'AB',\
                'O', 'A', 'B', 'O', 'B', 'AB']

blood_dict = {}

for b in blood_types:
    if b not in blood_dict:
        blood_dict[b] = 1
    elif b in blood_dict:
        blood_dict[b] += 1

print(blood_dict)
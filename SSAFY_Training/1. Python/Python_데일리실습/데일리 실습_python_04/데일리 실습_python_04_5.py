test_status = {
    '김코딩': 'solving',
   	'이싸피': 'solving',
   	'최이썬': 'cheating',
   	'오디비': 'sleeping',
   	'임온실': 'cheating',
   	'조실습': 'solving',
   	'박장고': 'sleeping',
   	'염자바': 'cheating'
}

cheat_lst = []
not_cheat_lst = {}
for keys in test_status:
	if test_status[keys] == 'cheating':
		cheat_lst.append(keys)
	else:
		not_cheat_lst[keys] = test_status[keys]
cheat_lst.sort()

for not_keys in not_cheat_lst:
	if not_cheat_lst[not_keys] == 'sleeping':
		not_cheat_lst[not_keys] = 'solving'
not_cheat_lst

print(cheat_lst)
print(f'test_status = {not_cheat_lst}')

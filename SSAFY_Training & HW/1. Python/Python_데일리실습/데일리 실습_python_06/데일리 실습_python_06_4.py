entry_record = ['이싸피', '박장고', '조실습', '이싸피', '조실습', '오디비', '임온실', '조실습', '조실습', '이싸피', '안도둑', '임온실', '최이썬', '오디비', '안도둑', '염자바', '박장고', '조실습',
                '최이썬', '조실습', '염자바', '박장고', '임온실', '임온실', '이싸피', '임온실', '오디비', '조실습', '염자바', '임온실', '박장고', '최이썬', '안도둑', '염자바', '임온실', '박장고', '이싸피', '안도둑',
                '임온실', '오디비', '최이썬', '안도둑', '이싸피', '오디비', '안도둑', '이싸피', '박장고', '박장고', '안도둑', '안도둑', '안도둑', '염자바', '최이썬', '오디비', '오디비', '최이썬', '이싸피', '임온실', '안도둑']

exit_record = ['최이썬', '조실습', '이싸피', '안도둑', '임온실', '안도둑', '이싸피', '오디비', '염자바', '박장고', '최이썬', '이싸피', '염자바', '염자바', '박장고', '임온실', '이싸피',
               '박장고', '안도둑', '염자바', '이싸피', '조실습', '조실습', '임온실', '박장고', '이싸피', '조실습', '박장고', '오디비', '안도둑', '조실습', '임온실', '안도둑', '안도둑', '임온실', '조실습', '최이썬', '안도둑', '임온실',
               '염자바', '이싸피', '임온실', '안도둑', '오디비', '안도둑', '오디비', '임온실', '염자바', '임온실', '박장고', '조실습', '이싸피', '최이썬', '최이썬', '오디비', '오디비', '염자바', '오디비', '안도둑', '박장고']


from collections import Counter

entry_lst_cnt = sorted(list(Counter(entry_record).items()),key = lambda x: x[1], reverse = True)
exit_lst_cnt = sorted(list(Counter(exit_record).items()),key = lambda x: x[1], reverse = True)

rank = 3
print(f'입장 기록 많은 Top{rank}')
for r in range(rank):
    print(f'{entry_lst_cnt[r][0]} {entry_lst_cnt[r][1]}회')

print('')
entry_lst_name = sorted(list(Counter(entry_record).items()),reverse = True)
exit_lst_name = sorted(list(Counter(exit_record).items()),reverse = True)

print('출입 기록이 수상한 사람')
for name in range(len(entry_lst_name)):
    if entry_lst_name[name][1] - exit_lst_name[name][1] > 0:
        print(f'{entry_lst_name[name][0]}은 입장 기록이 {entry_lst_name[name][1] - exit_lst_name[name][1]}회 더 많아 수상합니다.')
    
    elif entry_lst_name[name][1] - exit_lst_name[name][1] < 0:
        print(f'{entry_lst_name[name][0]}은 입장 기록이 {-(entry_lst_name[name][1] - exit_lst_name[name][1])}회 더 많아 수상합니다.')
    
    
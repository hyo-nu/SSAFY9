words_dict = {'proper' : '적절한',
'possible' : '가능한',
'moral' : '도덕적인',
'patient' : '참을성 있는',
'balance' : '균형',
'perfect' : '완벽한',
'logical' : '논리적인',
'legal' : '합법적인',
'relevant' : '관련 있는',
'responsible' : '책임감 있는',
'regular' : '규칙적인'}

ant_word = []
for i in words_dict:
    print(i[0])
    if i[0] == 'b' or i[0] == 'm' or i[0] == 'p':
        ant_word.append('im'+i)
    elif i[0] == 'l':
        ant_word.append('il'+i)
    elif i[0] == 'r':
        ant_word.append('ir'+i)

print(ant_word)
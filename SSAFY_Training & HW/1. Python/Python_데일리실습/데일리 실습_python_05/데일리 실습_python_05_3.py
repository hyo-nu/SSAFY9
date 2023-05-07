# 입력 예시
# s = '@#~I NeVEr DrEamEd AbouT SuCCeSs, i woRkEd foR iT.!>!'

# 출력 예시
# 'I never dreamed about success, i worked for it.'


s = '@#~I NeVEr DrEamEd AbouT SuCCeSs, i woRkEd foR iT.!>!'
S = list(s)
new_s = []

for i in S:
  if i.isalpha() == True or i == ' 'or i == '.'or i == ',':
    new_s.append(i)
last_s = ''.join(new_s)    

print(last_s.capitalize())


# A.    입력 예시 
# ['eat','tea','tan','ate','nat','bat']

# B.    출력 예시 
# [ ['eat', 'tea', 'ate'], ['tan', 'nat'], ['bat'] ] 

#group_anagrams

words = ['eat', 'tea' ,'tan', 'ate', 'nat', 'bat']
word_dict = {}

for word in words:
    lst_word = []
    
    key = ''.join(sorted(word))
    
    if key not in word_dict:
        word_dict[key] = word + ' '
    else: 
        word_dict[key] = word_dict[key] + word + ' '
        
for c in word_dict:
    word_dict[c] = word_dict[c].split()

print(word_dict.values())
words = ["round" , "dream", "magnet" , "tweet" , "tweet", "trick", "kiwi"]

for word in range(0,len(words)):
    # 같은단어 말한사람
    for check in range(0,word):
        if words[word] == words[check]:
            print(word)
   
    # 끝말잇기 틀린사람
    if word == 6:
        break        
    if words[word][len(words[word])-1] != words[word+1][0]:
        print(word+1) 
   
   
        
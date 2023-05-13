word1 = input('첫 번째 이름을 입력하세요 : ')
word2  = input('두 번째 이름을 입력하세요 : ')

# ord('문자') : 문자를 넣으면 유니코드 숫자로 반환해줌
# chr(정수) : 정수를 문자로 반환해줌

word1_lst = list(word1)
word2_lst = list(word2)

def chr_ord(word):
    word_ord = []
    for w in word:
        word_ord.append(ord(w))
    return word_ord

word1_lst_ord = (chr_ord(word1))
word2_lst_ord = (chr_ord(word2))

if sum(word1_lst_ord) > sum(word2_lst_ord):
    print(word1)
else:   
    print(word2)
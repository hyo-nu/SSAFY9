# 함수 내부에 불필요한 print문이 있는 경우 오답으로 처리가 됩니다.

def caesar(word, n):

    word_lst = list(word) # list로 변환
    password_lst = [] # 시저암호 list
    
    for word in word_lst:
        
        # 소문자
        if 97 <= ord(word) <= 122:
            if ord(word) + n > 122: # "z" 를 넘을 때
                password = chr(ord(word) + n - 26)
                password_lst.append(password)
            else:
                password = chr(ord(word) + n)
                password_lst.append(password)
        # 대문자            
        elif 65 <= ord(word) <= 90:
            if ord(word) + n > 90: # "Z"를 넘을 때
                password = chr(ord(word) + n - 26)
                password_lst.append(password)
            else:
                password = chr(ord(word) + n)
                password_lst.append(password)
            
    return ''.join(password_lst)

if __name__ == '__main__':
    print(caesar('apple', 5))      # fuuqj
    print(caesar('ssafy', 1))      # ttbgz
    print(caesar('Python', 10))    # Zidryx

amount = int(input("게시글의 총 갯수를 입력하세요 : "))
one_page = int(input("한 페이지에 필요한 게시글 수를 입력하세요 : "))

if amount % one_page == 0: #total page
    print(amount // one_page)
else:
    print(amount // one_page + 1)

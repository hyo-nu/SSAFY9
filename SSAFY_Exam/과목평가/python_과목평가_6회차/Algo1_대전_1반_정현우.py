Test = int(input())

for TC in range(Test):
    N = int(input())
    Str = input()
    Bin = bin(int(Str,16))[2:]                 # 이진수로 변환
    result = str(0) * (N * 4 - len(Bin)) + Bin # 사라진 0 뒤에 이어 붙히기
    result = result.split('0')                 # 0을 기준으로 나뉘는 새로운 리스트 생성
    result.sort(reverse=True)                  # 문자열 크기가 큰 순서대로 정렬

    print(f'#{TC+1}',len(result[0]))           # 첫번째 요소의 길이 출력
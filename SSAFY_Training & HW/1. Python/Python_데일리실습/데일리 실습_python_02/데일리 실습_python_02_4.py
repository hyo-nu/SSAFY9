# 출력 결과 예시
# 스테이크   50,000
# + VAT     7,500
# 총계 ₩    57,500

stake = int(input("stake 가격 : "))
vat = 0.15

print(f'스테이크 {format(stake,",")}')
print(f'+ VAT    {(format(round(stake * vat),","))}')
print(f'총계 ₩   {format(round(stake+stake*vat),",")}')
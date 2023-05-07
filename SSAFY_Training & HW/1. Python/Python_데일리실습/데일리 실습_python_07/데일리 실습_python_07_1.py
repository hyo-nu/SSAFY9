class Nationality():
    def __init__(self,Nationality):
        self.Nationality = Nationality
        
    def __str__(self):
        return f'나의 국적은 {self.Nationality}'       

korea_nationality = Nationality("대한민국")
print(korea_nationality) # 나의 국적은 대한민국

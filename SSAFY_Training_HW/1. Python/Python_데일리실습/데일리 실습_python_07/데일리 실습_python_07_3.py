# 1 + 2
# 2 – 1
# 3 * 4
# 4 / 0
class Calculator():
    def add(self,num1,num2):
        print(num1 + num2)

    def substract(self,num1,num2):
        print(num1 - num2)

    def multuply(self,num1,num2):
        print(num1 * num2)

    def divide(self,num1,num2):
        try:
            print(num1 / num2)
        except ZeroDivisionError:
            print('0으로 나눌 수 없습니다.')
c1 = Calculator()
c1.add(1,2)
c1.substract(2,1)
c1.multuply(3,4)
c1.divide(4,0)
# 입력 예시
# 2015
# 8
# 31

# 출력 예시 
#경고 월요일입니다.
#{'년': 2015, '월': 8, '일': 31, '요일': '월요일'}
import calendar
y = int(input())


while calendar.isleap(y) == True:
    print('윤년입니다. 연도를 다시 입력해주세요')
    y = int(input())
print(calendar.calendar(y))    
m = int(input())
d = int(input())    

week_list = ["월요일","화요일","수요일","목요일","금요일","토요일","일요일"]

if week_list[calendar.weekday(y,m,d)] == "월요일":
    print("경고 월요일입니다.")

dict_ymd = {'년' : y,'월' : m,'일' : d,'요일' : week_list[calendar.weekday(y,m,d)]}
print(dict_ymd)

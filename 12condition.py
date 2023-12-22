# if 문
# 특정 조건을 만족하면 지정한 문장(들)을 실행하는 조건문
# if 조건식:
#    수행할 문장(들)

# 속도위반 체크 프로그램
# 기준속도 : 50 km/h
speed = int(input('현재 속도는?'))

if speed >= 50:
    print('속도위반!!')

# 파이썬의 코드 블록
# 특정한 동작을 위한 관련 코드를 한곳에 모아둔 것
# 이러한 코드들은 반드시 같은 들여쓰기 내에 존재해야 함

# 조건식이 True인 경우 무조건 코드블록을 실행함
if True: print('Hello, World!!')

# if ~ else 문
# if문은 조건이 참일때만 지정한 코드를 실행하는데 비해
# if ~ else문은 조건이 참일때와 거짓일때 각각 지정한 코드를
# 실행한다는 것이 다름
# if 조건식:
#    수행할 문장1
# else:
#    수행할 문장2

# 자동온도 조절 프로그램
temp = int(input('기계온도는? '))

if temp >= 40:
    print("팬 가동~")
else:
    print("팬 중지~")

# 입력받은 정수를 3으로 나누고
# 소수점 첫째자리에서 반올림하기
num = int(input('정수 하나 입력하세요 '))
result = num / 3

if (result - int(result)) >= 0.5:
    result = int(result) + 1
else:
    result = int(result)

print(num, result)


# 중첩 if문
# if문 속에 또 다른 if문을 포함시켜 작성하는 조건문
# 조건문을 중첩할때는 들여쓰기에 유의해야 함
# 다양한 조건에 따라 결과를 처리하고 싶을때 사용 - 복잡함

# 평균이 73.5라 할때 조건에 따라
# 수/우/미/양/가 학점을
# 출력하는 조건문을 작성하세요
avg = 73.5

if avg >= 90: print('수')
else:
    if avg >= 80: print('우')
    else:
        if avg >= 70: print('미')
        else:
            if avg >= 60: print('양')
            else:
                print('가')


# 다중 if문
# 중첩 if문을 작성하는 경우 조건이 많으면 다소 복잡함
# 이러한 중첩 if문을 단순하게 작성할 수 있는 조건문

# if 조건식1:
#     실행할문장1
# elif 조건식2:
#     실행할문장2
# else:
#     실행할문장3

avg = 85.5

if avg >= 90: print('수')
elif avg >= 80: print('우')
elif avg >= 70: print('미')
elif avg >= 60: print('양')
else: print('가')

# 자동주문 시스템
intro = '''
  Good morning. Nice to meet you.
  Where are you from?
  Please select a number
'''

print(intro, end='')
menu = input('  1.대한민국  2.USA  3.中國 ')
if menu == '1': print('  주문하시겠어요?')
elif menu == '2': print('  Would you like to order?')
elif menu == '3': print('  您要訂購嗎？')
else: print('  Would you like to order?')

# bmi 지수에 따른 결과 출력
# 몸무게 / (키/100) ** 2
weight = float(input('몸무게는? '))
height = float(input('키는? '))
bmi = weight / (height / 100) ** 2

if bmi >= 35: result = '초고도비만'
elif bmi >= 30: result = '고도비만'
elif bmi >= 25: result = '비만'
elif bmi >= 23: result = '과체중'
elif bmi >= 18.5: result = '정상체중'
else: result = '저체중'

print(f'{weight} {height} {bmi:.0f} {result}')


# 누진세 적용 전기요금 계산
# 전기요금 = 기본요금 + (사용량 x 단가)
usage = int(input('전기 사용량은?'))

basic = 910
price = 99.3

if usage > 400:
    price = 280.6
    basic = 7300
elif usage > 200:
    price = 187.9
    basic = 1600

pay = basic + (usage * price)

print(f'{usage} {basic} {price} {pay}')


# 현재년도가 각각 1992, 2000, 2020(윤)과
# 1900, 2100(윤x)에 대해 윤년여부를 출력하는
# 조건식을 작성하세요
# 윤년1 : 4로 나눠 나머지가 0이고
#       100으로 나눠 나머지가 0이 아니면
# 윤년2 : 400으로 나눠 나머지가 0
year = int(input('년도는? '))

isLeap = '윤년 아님!'
cond1 = (year % 4 == 0) and (year % 100 != 0)
cond2 = year % 400 == 0

if cond1 or cond2:
    isLeap = '윤년 맞음!!'

print(f'{year} {isLeap}')

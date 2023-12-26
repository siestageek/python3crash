# 26 연봉과 결혼 여부 - 세금 계산
isMarried = input('결혼여부는? (1:미혼, 2:기혼) ')
sal = int(input('연봉은? '))

if isMarried == '1':
    if sal >= 3000: tax = sal * 0.25
    else: tax = sal * 0.1
else:
    if sal >= 6000: tax = sal * 0.35
    else: tax = sal * 0.15

print(f'{isMarried} {sal} {tax}')


# 33 숫자 6자리를 입력하면 신용카드의 종류와 은행정보
cardnum = input('카드번호는? ')

if cardnum == '356317': cardname = 'JCB카드 NH농협카드'
elif cardnum == '356901': cardname = 'JCB카드 신한카드'
elif cardnum == '356912': cardname = 'JCB카드 KB국민카드'
elif cardnum == '404825': cardname = '비자카드 비씨카드'
elif cardnum == '438676': cardname = '비자카드 신한카드'
elif cardnum == '457973': cardname = '비자카드 국민은행'
elif cardnum == '515594': cardname = '마스타카드 NH농협카드'
elif cardnum == '524353': cardname = '마스타카드 외환카드'
elif cardnum == '540926': cardname = '마스타카드 국민은행'

print(f'{cardnum} {cardname}')


# 35 시간때를 의미하는 영어단어
daytime = input('시간때는? ')

if daytime == 'morning hours': engdt = '아침시간 (7-12)'
elif daytime == 'midday' or daytime == 'noon': engdt = '점심시간 (12-1)'
elif daytime == 'afternoon hours': engdt = '오후 (1-6)'
elif daytime == 'evening hours': engdt = '저녁시간 (6-9)'
elif daytime == 'night hours': engdt = '밤시간 (9-12)'
elif daytime == 'midnight': engdt = '자정시간 (12)'
elif daytime == 'early morning hours': engdt = '새벽시간 (12-5)'
elif daytime == 'small hours': engdt = '새벽 (1-3)'
elif daytime == 'dawn' or daytime == 'daybreak': engdt = '해뜰력 (5-7)'

print(f'{daytime} {engdt}')


# 48 통장잔액이 25,000원, 은행이자가 연 6%라 할때
# 통장잔액이 지금의 2배를 넘는 시점은 언제인가?

account = 25000
interest = 1.06
limit = account * 2

for i in range(1, 20+1):
    account = account * interest
    print(f'{i} 년차 통장잔액 {account:,.0f}')


# 51 구구단 표
print('              Multiplication Table')
print('          1   2   3   4   5   6   7   8   9')
print('-------------------------------------------')
print('1  |      1   2   3   4   5   6   7   8   9')
print('2  |      2   4   6   8  10  12  14  16  18')
print('3  |      3   6   9  12  15  18  21  24  27')
print('4  |      4   8  12  16  20  24  28  32  36')
print('5  |      5  10  15  20  25  30  35  40  45')
print('6  |      6  12  18  24  30  36  42  48  54')
print('7  |      7  14  21  28  35  42  49  56  63')
print('8  |      8  16  24  32  30  48  56  64  72')
print('9  |      9  18  27  36  45  54  63  72  81')

print('              Multiplication Table')
print('          1   2   3   4   5   6   7   8   9')
print('-------------------------------------------')
for i in range(1, 9+1):
    print(f'{i}  |      {i}  {i*2:2d}  {i*3:2d}  {i*4:2d}'
          f'  {i*5:2d}  {i*6:2d}  {i*7:2d}  {i*8:2d}  {i*9:2d}')

print('              Multiplication Table')
print('          1   2   3   4   5   6   7   8   9')
print('-------------------------------------------')
for i in range(1, 9+1):
    print(f'{i}  |     ', end='')
    for j in range(1, 9+1):
        print(f'{i*j:2d}  ', end='')
    print()

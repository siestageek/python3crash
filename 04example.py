# 1
# 프로그래밍 언어 실습시 글꼴은
# 고정폭 글꼴을 사용할 것을 추천!
print('*   *    **    ****    ****    *   * ')
print('*   *   *  *   *   *   *   *   *   * ')
print('*****  *    *  ****    ****     * *  ')
print('*   *  ******  *   *   *   *     *   ')
print('*   *  *    *  *    *  *    *    *   ')

print('   /////   ')
print('  | o o |  ')
print(' (|  ^  |) ')
print('  | [_] |  ')
print('   -----   ')

print("  /\\_/\\   ")
print(" ( ' ' )  ")
print(" (  -  )  ")
print("  | | |   ")
print(" (__|__)  ")

# 3
rate1 = 1
# 1stPlayer = 2
# myprogram.java = 3
long = 4
TimeLimit = 5
numberOfWindows = 6

# 학생 테이블의 각 컬럼 데이터도
# 변수로 선언하고 값으로 초기화
stno = 1
hakbun = 201350050
name = '김태희'
addr = '경기도 고양시'
birth = '1985.3.22'
deptid = 1
profid = 4
regdate = '2023-12-20 14:43:15'

print(stno, hakbun, name, addr, birth)
print(stno, deptid, profid, regdate)

# 4
x, y, z = 1, 2, 3
s0, v0, t, g = 4, 5, 6, 9.8

print(3 * x, 3 * x + y, (x + y) / 7, (3 * x + y) / (z + 2))
print(s0 + v0 * t + (1/2) * g * t ** 2)

# 5
print(1 / 3, (1 / 3) * 3)  # 부동소수점 연산의 헛점이 원인
print(7 / 3, 7 % 3, 7 // 3)

result = 2
result /= 2    # result = result / 2
print(result)

# 6
x, y, m, n = 2.5, 1.5, 18, 4
print(x + n * y - (x + n) * y)
print(m / n + m % n)
print(5 * x - n / 5)
print( 1 - (1 - (1 - (1 - (1 - n)))) )

# 7
print(3 + 4.5 * 2 + 27 / 8)
print(True or False and 3 < 4 or not (5 == 7))
print(True or (3 < 5 and 6 >= 2))

# 논리연산이 가능하도록 bool 함수 사용
print(not True > bool('A'))
print(7 % 4 + 3 - 2 / 6 * bool('M'))
print(bool('D') + 1 + bool('M') % 2 / 3)

print(5.0 / 3 + 3 / 3)
print(53 % 21 < 45 / 18)
print((4 < 6) or True and False or False and (2 > 3))

print(7 - (3 + 8 * 6 + 3) - (2 + 5 * 2))

# 9
print(True and False and True or True)
print(True or True and True and False)
print((True and False) or (True and not False) or (False and not False) )
print((2 < 3) or (5 > 2) and not(4 == 4) or 9 != 4)
print(6 == 9 or 5 < 6 and 8 < 4 or 4 > 3)

# 10
print(27 / 13 + 4)
print(27 / 13 + 4.0)
print(42.7 % 3 + 18)
print(23 / 5 + 23 / 5.0)

print(2.0 + bool('a'))  # 문자와 숫자간 산술연산 불가
print(2 + bool('a'))

print('a' + 'b')

print(bool('a') / bool('b'))  # 문자끼리 산술연산 불가
print(float(bool('a') / bool('b')))

# 논리식과 산술식이 결합된 수식에서는
# 논리식의 결과가 True라면 값이 출력
# 논리식의 결과가 False라면 False가 출력
print((3 < 4) and 5 / 8)
print((3 > 4) and 5 / 8)
print('a' and not 'b')

# 11
name = '홍길동'
weight = 32.5
age = 19
print(name, weight, age)

# 12
# K-나이
# 세는나이 : 출생시 1살, 해가 지나면 +1
# 만나이 : 출생시 0살, 생일이 지나면 +1
# 연나이 : 현재년도 - 출생연도
birthYear = 2005
currentYear = 2023

age = currentYear - birthYear

print('연나이 : ', age)


# 13
print('7 x 1 = 7')
print('7 x 2 = 14')
print('7 x 3 = 21')
print('7 x 4 = 28')
print('7 x 5 = 35')
print('7 x 6 = 42')
print('7 x 7 = 49')
print('7 x 8 = 56')
print('7 x 9 = 63')

dan = 5
print(f'{dan} x 1 = {dan * 1}')
print(f'{dan} x 2 = {dan * 2}')
print(f'{dan} x 3 = {dan * 3}')
print(f'{dan} x 4 = {dan * 4}')
print(f'{dan} x 5 = {dan * 5}')
print(f'{dan} x 6 = {dan * 6}')
print(f'{dan} x 7 = {dan * 7}')
print(f'{dan} x 8 = {dan * 8}')
print(f'{dan} x 9 = {dan * 9}')

print('%d x 1 = %d' % (dan, dan*1))
print('%d x 2 = %d' % (dan, dan*2))
print('%d x 3 = %d' % (dan, dan*3))
print('%d x 4 = %d' % (dan, dan*4))
print('%d x 5 = %d' % (dan, dan*5))
print('%d x 6 = %d' % (dan, dan*6))
print('%d x 7 = %d' % (dan, dan*7))
print('%d x 8 = %d' % (dan, dan*8))
print('%d x 9 = %d' % (dan, dan*9))

print('{} x 1 = {}'.format(dan, dan * 1))
print('{} x 2 = {}'.format(dan, dan * 2))
print('{} x 3 = {}'.format(dan, dan * 3))
print('{} x 4 = {}'.format(dan, dan * 4))
print('{} x 5 = {}'.format(dan, dan * 5))
print('{} x 6 = {}'.format(dan, dan * 6))
print('{} x 7 = {}'.format(dan, dan * 7))
print('{} x 8 = {}'.format(dan, dan * 8))
print('{} x 9 = {}'.format(dan, dan * 9))

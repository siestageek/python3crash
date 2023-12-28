# 함수와 모듈
# 함수는 일정한 작업을 수행하는 코드 집합체
# 보통 여러 곳에 반복적으로 사용되는 코드들을 함수로 정의해서 사용

# 즉, 여러 곳에 반복적으로 사용할 가치가 있는 코드를 한 뭉치로 묶고
# (어떤 입력값을 주면) 결과가 반환되도록 사용

# 또한, 여러 코드들을 함수화하면 프로그램의 흐름을
# 일목요연하게 파악하기 쉬움

# 코드의 이식성이나 재사용성이 높아짐 - 개발 속도가 빨라짐

# 다른 사람과의 협업시 코드가 섞이지 않게 하기 위한
# 목적도 있음 - 모듈

print('선생님~ 미워요!')  # 단순출력

print('선생님~ 미워요!')  # 반복출력
print('선생님~ 미워요!')
print('선생님~ 미워요!')

for _ in range(3):      # 개선된 반복
    print('선생님~ 미워요!')

# 이러한 반복문을 여러번 사용해야 한다면?
# 또, 만약, '미워요' 대신 '싫어요'나 '좋아요'로 바꿔야 한다면?
# => 함수를 이용!

# 함수 정의
# def 함수명(매개변수):
#     함수몸체(코드들)

def saymsg():   # 입력값x, 함수내에서 출력처리 (반환값x)
    for _ in range(3):  # 개선된 반복
        print('선생님~ 미워요!')

# 함수 호출
# 함수명(), 함수명(입력값)
saymsg()

def saymsg2():
    msg = '싫어요'
    for _ in range(3):  # 개선된 반복
        print(f'선생님~ {msg}!')

saymsg2()


def saymsg3(msg):   # 입력값o, 함수내에서 출력처리 (반환값x)
    for _ in range(3):  # 개선된 반복
        print(f'선생님~ {msg}!')
        
saymsg3('좋아요')
saymsg3('미워요')
saymsg3('싫어요')


# 함수 이름 짓기
def SensorOn():
    print('온도 센서 작동을 시작한다')

def SensorOff():
    print('온도 센서 작동을 중지한다')


length = int(input('길이를 입력하세요. (cm) '))
# 1cm = 0.393701
print(f'{length} cm = {length * 0.393701:.4f} inch')

def notebookSize():
    print('길이를 입력하세요. (cm) ', end=' ')
    length = int(input())
    cm2inch = length * 0.393701
    print(f'{length} cm = {cm2inch:.4f} inch')

notebookSize()


times = int(input('이동 시간을 입력하세요'))
speed = int(input('이동 속도를 입력하세요'))
dist = times * speed
print(f'이동거리는 {dist:.1f} km 입니다.')


def movedist():
    times = int(input('이동 시간을 입력하세요'))
    speed = int(input('이동 속도를 입력하세요'))
    dist = times * speed
    print(f'이동거리는 {dist:.1f} km 입니다.')

movedist()


# 함수의 유형
# 입력값 x   반환값 x
# 입력값 x   반환값 o   !!
# 입력값 o   반환값 x
# 입력값 o   반환값 o   !!!

def saymsg4(msg):   # 입력값o, 처리 결과 반환 (반환값o)
    text = ''
    for _ in range(3):  # 개선된 반복
        text += f'선생님~ {msg}!\n'
    return text  # 결과를 처리하지 않고 넘김

print(saymsg4('미워요'))


def notebookSize2():
    print('길이를 입력하세요. (cm) ', end=' ')
    length = int(input())
    cm2inch = length * 0.393701
    return cm2inch

print(f'{notebookSize2():.1f} inch')
print(f'{notebookSize2():.1f} 인치')

def notebookSize3():
    print('길이를 입력하세요. (cm) ', end=' ')
    length = int(input())
    cm2inch = length * 0.393701
    return length, cm2inch

length, cm2inch = notebookSize3()
print(f'{length} cm = {cm2inch:.4f} inch')
print(f'{length} 센티미터 = {cm2inch:.4f} 인치')


def movedist2():
    times = int(input('이동 시간을 입력하세요'))
    speed = int(input('이동 속도를 입력하세요'))
    dist = times * speed
    return dist

dist = movedist2()
print(f'이동거리는 {dist:.1f} km 입니다.')


# 계산기 프로그램
op1 = int(input('숫자를 입력하세요. '))
op2 = input('연산자를 선택하세요. 1.덧셈 2.뺄셈 3.곱셈 4.나눗셈 ')
op3 = int(input('숫자를 입력하세요. '))

result = 0
if op2 == '1': 
    result = op1 + op3
    op2 = '덧셈'
elif op2 == '2': 
    result = op1 - op3
    op2 = "뺄셈"
elif op2 == '3': 
    result = op1 * op3
    op2 = "곱셈"
elif op2 == '4': 
    result = op1 / op3
    op2 = "나눗셈"

print(f'{op2} 결과 : {result:.1f} ')

# 프로그램 객체지향 설계 5원칙
# SOLID

def readData():
    op1 = int(input('숫자를 입력하세요. '))
    op2 = input('연산자를 선택하세요. 1.덧셈 2.뺄셈 3.곱셈 4.나눗셈 ')
    op3 = int(input('숫자를 입력하세요. '))
    return op1, op2, op3


def computeNumber(op1, op2, op3):
    result = 0
    if op2 == '1':
        result = op1 + op3
        op2 = '덧셈'
    elif op2 == '2':
        result = op1 - op3
        op2 = "뺄셈"
    elif op2 == '3':
        result = op1 * op3
        op2 = "곱셈"
    elif op2 == '4':
        result = op1 / op3
        op2 = "나눗셈"

    return op2, result


def computer():
    # 데이터 입력부
    op1, op2, op3 = readData()

    # 데이터 계산
    op2, result = computeNumber(op1, op2, op3)
    
    # 처리 결과 넘김
    return op2, result 


op2, result = computer()    
print(f'{op2} 결과 : {result:.1f} ')


# 함수에 값 전달하기
# 매개변수parameter : 함수 정의시 함수에서 사용할 변수 정의
# 매개변수는 함수 호출시 전달받은 인수로 초기화되어 사용됨
# 인수argument : 함수 호출시 매개변수에 전달할 실제 값


# 단위환산 프로그램
mm = int(input('길이(mm)를 입력하세요'))

cm = mm * 0.1
m = mm * 0.001
inch = mm * 0.03937
ft = mm * 0.003281

print(f'''
{mm} mm -> {cm} cm
{mm} mm -> {m} m
{mm} mm -> {inch} inch
{mm} mm -> {ft} ft ''')


def readMM():
    mm = int(input('길이(mm)를 입력하세요'))
    return mm


def convertAll(mm):
    cm = mm * 0.1
    m = mm * 0.001
    inch = mm * 0.03937
    ft = mm * 0.003281

    return mm, cm, m, inch, ft


def convertUnit():
    mm = readMM()

    return convertAll(mm)


mm, cm, m, inch, ft = convertUnit()
print(f'''
{mm} mm -> {cm} cm
{mm} mm -> {m} m
{mm} mm -> {inch} inch
{mm} mm -> {ft} ft ''')


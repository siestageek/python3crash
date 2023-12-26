# 슬라이싱(slicing)
# 연속적인 객체들(리스트,튜플,문자열)에 범위를 지정하고
# 선택해서 부분적으로 객체를 가져오는 방법 및 표기법
# 리스트 객체에서 필요한 부분의 항목만 뽑아 사용하는 것
# 객체명[시작:끝-1:스텝]

# 다음 코드에서 생년월일 추출
jumin = '123456-1234567'  

print(jumin[0:6])
print(jumin[:6])   # 시작을 생략하면 리스트의 인덱스는 0부터

# 생년월일과 - 를 제외한 나머지 추출
print(jumin[7:14])
print(jumin[7:])  # 끝을 생략하면 리스트의 맨 마지막 문자까지

# 코드에서 짝수/홀수 위치의 문자 추출
print(jumin[0:14:2])   # 홀수 위치 문자 추출
print(jumin[0::2])
print(jumin[::2])

print(jumin[1:14:2])   # 짝수 위치 문자 추출
print(jumin[1::2])

# 역순으로 추출 : step을 -로 설정
print(jumin[14:0:-1])
print(jumin[14::-1])
print(jumin[::-1])

# 확인 문제
alphabet = ['a','b','c','d','e','f','g','h','i','j']

# 역순 출력
print(alphabet[:])
print(alphabet[::-1])

# 요구사항에 따라 출력
print(alphabet[2:5+1])
print(alphabet[:4+1])
print(alphabet[3:7+1])
print(alphabet[5:])
print(alphabet[3:8+1])


# 33 숫자 6자리를 입력하면 신용카드의 종류와 은행정보
cardnum = input('카드번호는? ')

if cardnum[:2] == '35':
    if cardnum == '356317': cardname = 'JCB카드 NH농협카드'
    elif cardnum == '356901': cardname = 'JCB카드 신한카드'
    elif cardnum == '356912': cardname = 'JCB카드 KB국민카드'
elif cardnum[:1] == '4':
    if cardnum == '404825': cardname = '비자카드 비씨카드'
    elif cardnum == '438676': cardname = '비자카드 신한카드'
    elif cardnum == '457973': cardname = '비자카드 국민은행'
elif cardnum[:1] == '5':
    if cardnum == '515594': cardname = '마스타카드 NH농협카드'
    elif cardnum == '524353': cardname = '마스타카드 외환카드'
    elif cardnum == '540926': cardname = '마스타카드 국민은행'

print(f'{cardnum} {cardname}')

# 리스트 합치기 : extend, +
a = [1, 2, 3]
b = [4, 5, 6]
c = ['7', '8', '9']

a.extend(b)   # a = a + b
print(a)

b.extend(c)
print(b)

# 리스트의 특정 요소 존재 파악 : in/not in
todo = ['cleaning', 'shoping', 'study', 'exercise', 'game']

print('drive' in todo)
print('shoping' in todo)

# 리스트의 모든 요소 존재 순회
for item in todo:
    print(item, end=' ')

# 리스트의 모든 요소 존재 순회 : enumerate (항목의 인덱스도 출력)
for idx, item in enumerate(todo):
    print(idx, item)

# 리스트의 모든 요소 제거 : clear
print(todo)
todo.clear()
print(todo)

# 혈액형 보관 시스템
bloods = []
a, b, ab, o = 0, 0, 0, 0

for idx in range(1, 10+1):
    print(f'헌혈해 주셔서 감사합니다. 혈액형을 선택하세요 ({idx}/10)')
    blood = input('A, B, AB, O : ')
    bloods.append(blood)

for bd in bloods:
    if bd == 'A': a += 1
    elif bd == 'B': b += 1
    elif bd == 'AB': ab += 1
    elif bd == 'O': o += 1

print(f'''
-------------------
혈액형 : 개수
-------------------
A형  : {a}
B형  : {b}
AB형 : {ab}
O형  : {o}
-------------------''')

# 리스트의 항목별 빈도 계산 : count(값)
bloods.count('A')
bloods.count('B')
bloods.count('AB')
bloods.count('O')



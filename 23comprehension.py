# 컴프리헨션comprehension - 반복문 축약
# 다양한 데이터 객체에 사용되는 복잡한 구문을
# 단순하게 작성할 수 있도록 지원하는 기능

# 파이썬에는 4가지 종류의 축약을 지원
# list(py2), set(py3), dict(py3), generator(py3)

# 리스트에 적용하는 축약
# 1 ~ 10 까지의 정수를 리스트에 저장
a = list(range(1, 10+1))
print(a)

b = []
for i in range(1, 10+1):
    b.append(i)
print(b)

# 리스트 for 축약문
# [ 표현식 for 항목 in 반복가능객체 ]
c = [ i for i in range(1, 10+1) ]
print(c)

# 1 ~ 10 까지 제곱값을 리스트로 생성하는 축약문 작성
d = []
for i in range(1, 10+1):
    d.append( i ** 2 )
print(d)

e = [ i ** 2 for i in range(1, 10+1) ]
print(e)

# ex) 다음 리스트를 이용해서 제곱값을 계산하고
# 새로운 리스트에 생성하세요
val1 = [1, 2, 3, 4, 5]
val2 = [1, 2, 'A', False, 9, 100]

f = []
for val in val1:
    f.append(val ** 2)
print(f)

g = [ val ** 2 for val in val1 ]
print(g)

h = [ val ** 2 for val in val2 ]  # 오류발생!
print(h)

i = []
for val in val2:
    if type(val) == int:
        i.append(val ** 2)
print(i)

# for if 축약문
# [ 표현식 for 항목 in 반복가능객체 if 조건 ]
j = [ val ** 2 for val in val2 if type(val) == int]
print(j)


# 1 ~ 100사이 정수 중 홀수만 골라서 리스트에 저장
k = [i for i in range(1, 100+1) if i % 2 != 0]
print(k)

# 1 ~ 100 사이의 정수 중 임의의 정수가 짝수면 even,
# 홀수면 odd 라고 구분해서 리스트에 저장하세요

l = []
for i in range(1, 100+1):
    if i % 2 == 0: l.append('even')
    else: l.append('odd')
print(l)

# for 다중 if 축약문
# [ 표현식 if 조건 else 거짓일때표현식
#                for 항목 in 반복가능객체 ]
m = [ 'even' if i % 2 == 0 else 'odd'
             for i in range(1,100+1) ]
print(m)

# 구구단 중 7,8단의 결과를 리스트에 저장
# 7 x 1 = 7, 7 x 2 = 14, ~ , 7 x 9 = 63
# 8 x 1 = 8, 8 x 2 = 16, ~ , 8 x 9 = 72
n = []
for i in range(7, 8+1):
    for j in range(1, 9+1):
        n.append(i * j)
print(n)

# 다중 for 축약문
# [ 표현식 for 항목1 in 반복가능객체1
#         for 항목2 in 반복가능객체2 ]
o = [ i * j  for i in range(7, 8+1)
             for j in range(1, 9+1) ]
print(o)


# name, grd 리스트의 값들을
# 각각의 키와 값으로 딕셔너리를 만즐어 저장하시오
name = ['혜교','수지','지현']
grd = ['우','미','수']

# 단순하고 무식한 버젼
sj = {}
sj[name[0]] = grd[0]
sj[name[1]] = grd[1]
sj[name[2]] = grd[2]
print(sj)

# 반복문 버젼
sj = {}
for i in range(len(name)):
    sj[name[i]] = grd[i]
print(sj)

# 딕셔너리 for 축약문 - {} 사용
# { 키값표현식 for key, val in
#                  zip(반복객체1, 반복객체2) }
# zip : 동일한 갯수의 시퀀스 자료형을 하나로
#       묶어주는 역할을 수행
# zip([1,2,3], ['a','b','c'])
# => [(1,'a'),(2,'b'),(3,'c')]
sj = { key:val for key, val in zip(name, grd) }
print(sj)

# 학생과 국어점수에 대한 리스트가 있을때
# 학생은 키로, 값은 합격여부로 하는 딕셔너리를 생성하세요
# 단, 국어점수가 85점이상인 경우 '합격',
#     그외는 '불합격'이라고 출력함
std = ['철수', '영희', '길동', '꺽정']
kor = [50, 80, 90, 60]

results = {}
for i in range(len(std)):
    result = '불합격'
    if kor[i] >= 85: result = '합격'
    results[std[i]] = result

print(results)

# 딕셔너리 for if 축약문 - {} 사용
# { 키 참일때표현식 if 조건 else 거짓일때표현식
#    for key, val in zip(반복객체1, 반복객체2) }
results = { k: '합격' if v >= 85 else '불합격'
            for k, v in zip(std, kor) }
print(results)

# 파이썬으로 JSON 형식 다루기
# javascript object notation
# 자바스크립트에서 객체를 표현하는 방식을 이용해서
# 각종 프로그래밍 언어에서 데이터를 표현함
# 예전에는 csv, xml로 데이터를 표현했다면
# 지금은 json으로 거의 대부분 이용해서 표현
# NoSQL 데이터베이스 중에서 MongoDB나 neo4j 역시
# 데이터를 다룰때에는 json형식을 주로 사용

# json은 파이썬의 dict 자료형과 유사
# [ {'키':'값, {...}, {...} ]
# { 'userid':'abc123', 'passwd':'987xyz',
#   'email':'abc123@xyz987.com' }

# csv 표기법
# userid,passwd,email
# abc123,987xyz,abc123@xyz987.com

# xml 표기법
# <data>
# <userid>abc123</userid>
# <passwd>987xyz</passwd>
# <email>abc123@xyz987.com</email>
# </data>

# 파이썬에서 json 패키지 불러오기
import json
# JSON 파일을 만들기 위해 dict 패키지 불러오기
from collections import OrderedDict

# json 객체 생성 1 - text 이용
# python의 dict 처럼 정의
member = {'userid': 'abc123', 'passwd': '987xyz',
          'email': 'abc123@xyz987.com'}

# dumps 함수를 이용하면 파이썬에서 만든 dict객체를
# json 객체로 만들수 있음
obj = json.dumps(member)
print(obj)

# json 객체 생성 2 - OrderedDict 이용
# python의 dict보다 효율적으로 dict 객체 생성 가능
person = OrderedDict()
person['name'] = '혜교'
person['phone'] = '123-4567-8912'
person['friends'] = ['지현', '수지']

schools = OrderedDict()
schools['mid'] = '서울중학교'
schools['high'] = '서울고등학교'
person['schools'] = schools

obj = json.dumps(person, ensure_ascii=False)  # 한글 출력 가능
print(obj)

# 메모리에 생성된 json객체를 파일에 저장
# dump(json객체, 파일객체, 옵션)
with open('person.json', 'w', encoding='UTF-8') as f:
    json.dump(person, f, ensure_ascii=False)

# 파일에 생성된 json객체를 메모리로 불러옴
# load(파일객체)
with open('person.json', encoding='UTF-8') as f:
    person_data = json.load(f)

print(person_data)



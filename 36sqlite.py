# 파이썬 데이터베이스 프로그래밍
# 데이터의 영속성을 부여하는 방법 중 하나
# 작은 양의 데이터는 파일입출력을 통해 처리 가능
# 대량의 데이터를 체계적으로 저장해서 원하는 목적에 따라
# 데이터를 처리(검색,수정,삭제)할 수 있도록 해 줌

# 파이썬에서는 일반적인 관계형 데이터베이스를 이용해서
# 데이터를 저장,검색,수정,삭제할 수 있음
# 또한, 독립적인 데이터베이스 서버없이 파일기반
# 데이터베이스를 이용해서 간편하게 데이터를 조작할 수도 있음
# 내장형 파일기반 데이터베이스 : sqlite

# sqlite
# 내장형 파일기반 데이터베이스
# 서버가 필요없고 복잡한 설정도 필요없으면서
# 트랜잭션이 지원되는 데이터베이스
# 하나의 파일에 테이블,뷰,색인,트리거등이 저장
# 용량이 작아 메모리에 올리기도 쉽고 속도도 빠른편
# 안드로이드, ios에는 기본적으로 포함되어 있음
# 단, 복잡하고 용량이 큰 데이터를 저장하기에는 다소 적절치 않음
# sqlite.org

# sqlite 설치법
# sqlite-tools-win-x64-3440200.zip  (2024.1.4기준)
# 압축해제 후 sqlit3.exe를 c:/Java/sqlite 에 저장
# 명령프롬프트에서 sqlite3.exe를 실행 함
# => cd \Java\sqlite
# => sqlite3

# 데이터베이스 생성 : .open 디비명.db
# .open bigdata.db

# 테이블 생성 : create table
# create table member (
#     userid varchar(18) primary key,
#     passwd varchar(18) not null,
#     name varchar(18) not null,
#     email varchar(18) not null
# );

# 테이블 목록 확인 : .table

# 테이블 구조 확인 : pragma table_info('테이블명');
# pragma table_info('member');

# 조회시 컬럼헤더 설정
# .header on
# .mode column

# 데이터 삽입 : insert
# insert into member values
# ('abc123','987xyz','abc123','abc123@987xyz.co.kr');

# 데이터 조회 : select
# select * from member;

# .csv 파일 가져오기 import
# .mode csv
# .import csv파일명 테이블명
# .import c:/Java/EMPLOYEES.csv employees

# tsv 파일 가져오기 import
# .mode tabs
# .import tsv파일명 테이블명
# .import c:/Java/zipcode_20130201(2).txt zipcode2013

# 단, import시 csv, tsv파일의 인코딩은 UTF-8이어야 함!!

# sqlite 종료 : .quit

# 파이썬으로 sqlite 다루기 1 - select
import sqlite3

# 데이터베이스 연결
conn = sqlite3.connect('db/bigdata.db')

# SQL 실행을 위해 커서 생성
cursor = conn.cursor()

# 실행할 SQL문을 작성하고
# 실행후 결과를 커서에 저장
sql = 'select * from zipcode2013 where dong like "자양1%"'
cursor.execute(sql)

# 반복문을 이용해서 커서에 저장된
# 결과집합으로부터 한 행씩 읽어서 처리
while True:
    row = cursor.fetchone()
    if not row: break

    result = (f'{row[0]} {row[1]} {row[2]} '
              f'{row[3]} {row[4]} {row[5]}')
    print(result)

# 작업이 끝나면 커서와 접속을 닫음
cursor.close()
conn.close()


# 파이썬으로 sqlite 다루기 2 - 직책별 사원수 조회 (employees)
conn = sqlite3.connect('db/bigdata.db')

cursor = conn.cursor()

sql = (' select job_id, count(first_name) as emps from employees '
       ' group by job_id order by emps desc ')
cursor.execute(sql)

result = ''
while True:
    row = cursor.fetchone()
    if not row: break

    result += f'{row[0]} {row[1]}\n'

print(result)

cursor.close()
conn.close()


# 국가별 메달별 획득수 조회
conn = sqlite3.connect('db/bigdata.db')
cursor = conn.cursor()

sql = ' select Country, Medal, count(Country) as Cnt '\
      ' from summermedals group by Country, Medal '\
      ' order by Cnt desc limit 0, 15 '
cursor.execute(sql)

result = ''
while True:
    row = cursor.fetchone()
    if not row: break

    result += f'{row[0]} {row[1]} {row[2]}\n'

print(result)

cursor.close()
conn.close()


# 사원이름, 성, 직책, 연봉, 부서명 조회
conn = sqlite3.connect('db/bigdata.db')
cursor = conn.cursor()

sql = ' select first_name, last_name, job_id, salary, department_name '\
      ' from employees e inner join main.departments d '\
      ' on e.DEPARTMENT_ID = d.department_id '\
      ' limit 0, 20 '
cursor.execute(sql)

result = ''
while True:
    row = cursor.fetchone()
    if not row: break

    result += f'{row[0]} {row[1]} {row[2]} {row[3]} {row[4]}\n'

print(result)

cursor.close()
conn.close()



